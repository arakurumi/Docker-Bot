FROM arakurumi/myne:ubuntu AS builder

COPY . /

RUN apt install --yes build-essential libfreetype6-dev libjpeg-dev python3-venv

RUN python -m venv --system-site-packages gemoe

RUN /gemoe/bin/pip install --no-cache-dir --requirement requirements.txt

RUN apt remove --yes build-essential libfreetype6-dev libjpeg-dev

FROM arakurumi/myne:ubuntu

COPY --from=builder / /

CMD ["/usr/bin/sh"]
