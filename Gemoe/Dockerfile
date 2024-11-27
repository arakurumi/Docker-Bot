FROM arakurumi/myne:ubuntu

COPY . .

RUN apt-get --yes install python3-venv

RUN python -m venv --system-site-packages gemoe

RUN gemoe/bin/pip install --no-cache-dir --requirement requirements.txt