FROM arakurumi/mltb:latest AS builder

COPY . /

RUN sed -i 's/\r$//' *.sh

RUN sh patch.sh

RUN python -m venv --system-site-packages mltb

RUN /mltb/bin/pip install --no-cache-dir --requirement requirements.txt

FROM arakurumi/mltb:latest

COPY --from=builder / /

CMD ["/bin/sh"]
