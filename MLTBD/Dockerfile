FROM arakurumi/mltb:latest

WORKDIR /app

RUN chmod -R 777 /app

COPY . .

RUN sh patch.sh

RUN python -m venv --system-site-packages mltb

RUN mltb/bin/pip install --no-cache-dir --requirement requirements.txt

CMD ["sh", "start.sh"]
