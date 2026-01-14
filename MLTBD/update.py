from base64 import b64decode
from uvloop import install  # type: ignore

install()

from http.client import responses  # noqa: E402
from importlib import import_module  # noqa: E402
from logging import (  # noqa: E402
    ERROR,
    INFO,
    basicConfig,
    getLogger,
)
from os import getenv  # noqa: E402
from pathlib import Path  # noqa: E402
from subprocess import run  # noqa: E402

from pymongo.mongo_client import MongoClient  # noqa: E402
from pymongo.server_api import ServerApi  # noqa: E402
from requests import get  # noqa: E402

basicConfig(
    format="{asctime} - [{levelname[0]}] {name} [{module}:{lineno}] - {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    style="{",
    level=INFO,
)

LOGGER = getLogger("update")
getLogger("pymongo").setLevel(ERROR)

if Path("log.txt").exists():
    with Path("log.txt").open(mode="r+") as file:
        file.truncate(0)

if Path("alog.txt").exists():
    Path("alog.txt").unlink(missing_ok=True)

if Path("rlog.txt").exists():
    Path("rlog.txt").unlink(missing_ok=True)

if not Path("config.py").exists():
    if CONFIG_URL := getenv(
        "CONFIG_URL",
        "https://gist.githubusercontent.com/arakurumi/d9d010eec12f913b0e76176685c74a10/raw/config.py",
    ):
        LOGGER.info("CONFIG_URL is found! Downloading CONFIG_URL...")

        req = get(
            url=CONFIG_URL,
            timeout=10,
            allow_redirects=True,
        )

        if req.ok:
            with Path("config.py").open(mode="wb+") as file:
                file.write(req.content)

        else:
            LOGGER.error(f"[{req.status_code}] {responses[req.status_code]}")

    else:
        LOGGER.warning("CONFIG_URL is not found! Using local config.py instead...")


def load_config() -> dict:
    try:
        settings = import_module("config")
        config_file = {
            key: value.strip() if isinstance(value, str) else value
            for key, value in vars(settings).items()
            if not key.startswith("__")
        }
        return config_file

    except ModuleNotFoundError:
        LOGGER.info("Config module not found! Loading from environment variables...")
        return {
            "BOT_TOKEN": getenv("BOT_TOKEN", ""),
            "DATABASE_URL": getenv("DATABASE_URL", ""),
            "UPSTREAM_BRANCH": getenv("UPSTREAM_BRANCH", "master"),
            "UPSTREAM_REPO": getenv("UPSTREAM_REPO", ""),
        }


config_file = load_config()
BOT_TOKEN = config_file.get("BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    LOGGER.error("BOT_TOKEN is not found!")
    exit(1)

BOT_ID = BOT_TOKEN.split(":", 1)[0]

DATABASE_URL = config_file.get("DATABASE_URL", "").strip()
DATABASE_NAME = config_file.get("DATABASE_NAME", "mltb").strip()

if DATABASE_URL and DATABASE_NAME:
    try:
        conn = MongoClient(
            DATABASE_URL,
            server_api=ServerApi("1"),
        )

        db = conn.mltb
        old_config = db.settings.deployConfig.find_one({"_id": BOT_ID}, {"_id": 0})
        config_dict = db.settings.config.find_one({"_id": BOT_ID})

        if (
            old_config is not None and old_config == config_file or old_config is None
        ) and config_dict is not None:
            config_file["UPSTREAM_REPO"] = config_dict["UPSTREAM_REPO"]
            config_file["UPSTREAM_BRANCH"] = config_dict["UPSTREAM_BRANCH"]

        conn.close()

    except Exception as e:
        LOGGER.error(f"DATABASE ERROR! ERROR: {e}")

UPSTREAM_REPO = config_file.get("UPSTREAM_REPO", "").strip()
try:
    UPSTREAM_REPO = b64decode(UPSTREAM_REPO).decode("UTF-8")
except Exception:
    pass

UPSTREAM_BRANCH = config_file.get("UPSTREAM_BRANCH", "").strip() or "master"

if UPSTREAM_REPO and UPSTREAM_BRANCH:
    if Path(".git").exists():
        run(args=["rm -rf .git"], shell=True)

    process = run(
        args=[
            f"git init -q \
            && git config --global user.email kqruumi@gmail.com \
            && git config --global user.name KQRM \
            && git add . \
            && git commit -sm update -q \
            && git remote add origin {UPSTREAM_REPO} \
            && git fetch origin -q \
            && git reset --hard origin/{UPSTREAM_BRANCH} -q"
        ],
        shell=True,
    )

    if process.returncode == 0:
        LOGGER.info("Successfully updated with latest commit from UPSTREAM_REPO!")
        process = run(
            args=["git log -1 --pretty=format:'%s'"],
            capture_output=True,
            shell=True,
            text=True,
        )

        if process.returncode == 0:
            LOGGER.info(f"UPDATE: {process.stdout}")

    else:
        LOGGER.error(
            "Something wrong while updating! Check UPSTREAM_REPO if valid or not!"
        )

else:
    LOGGER.warning("UPSTREAM_REPO is not found!")
    LOGGER.warning("UPSTREAM_BRANCH is not found!")
