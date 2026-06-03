FROM arakurumi/myne:ubuntu AS builder

COPY . /

RUN apt-get install --yes build-essential python3-venv

RUN python -m venv --system-site-packages music

RUN /music/bin/pip install --no-cache-dir --requirement requirements.txt

RUN apt remove --yes build-essential

FROM arakurumi/myne:ubuntu

COPY --from=builder / /

CMD ["/usr/bin/sh"]
