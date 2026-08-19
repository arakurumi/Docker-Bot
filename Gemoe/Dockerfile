FROM arakurumi/myne:debian AS builder

COPY . /

RUN apt update && apt install --yes libfreetype6-dev libjpeg-dev

RUN python -m venv --system-site-packages gemoe

RUN /gemoe/bin/pip install --no-cache-dir --requirement requirements.txt

RUN apt remove --yes libfreetype6-dev libjpeg-dev && rm -rf /var/lib/apt/lists /var/cache/apt /tmp/* /root/.cache

FROM arakurumi/myne:debian

COPY --from=builder / /

CMD ["/usr/bin/sh"]
