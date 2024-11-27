FROM arakurumi/myne:ubuntu

COPY . .

RUN apt-get install python-venv

RUN python -m venv --system-site-packages gemoe

RUN gemoe/bin/pip install --no-cache-dir --requirement requirements.txt