FROM arakurumi/mltb:latest AS builder

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    TZ=Asia/Jakarta

COPY . /

RUN python -m venv --system-site-packages mltb

RUN /mltb/bin/pip install --no-cache-dir --requirement requirements.txt

FROM arakurumi/mltb:latest

COPY --from=builder / /

CMD ["/bin/sh"]