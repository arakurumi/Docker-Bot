FROM arakurumi/mltb:latest AS builder

COPY . /

RUN apk add --no-cache --virtual BuildDependency clang compiler-rt curl-dev linux-headers python3-dev

RUN python -m venv --system-site-packages mltb

RUN /mltb/bin/pip install --no-cache-dir --requirement requirements.txt

RUN apk del BuildDependency

FROM arakurumi/mltb:latest

COPY --from=builder / /

CMD ["/bin/sh"]
