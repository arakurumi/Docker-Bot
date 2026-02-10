FROM arakurumi/myne:ubuntu AS builder

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    TZ=Asia/Jakarta

COPY . /

RUN apt-get install --yes python3-venv

RUN python -m venv --system-site-packages music

RUN /music/bin/pip install --no-cache-dir --requirement requirements.txt

FROM arakurumi/myne:ubuntu

COPY --from=builder / /

CMD ["/usr/bin/sh"]
