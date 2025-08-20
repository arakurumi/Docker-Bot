FROM arakurumi/mltb:latest

WORKDIR /app

RUN chmod -R 777 /app

COPY . .

RUN sh patch.sh

RUN pip install --break-system-packages --no-cache-dir --requirement requirements.txt

CMD ["sh", "start.sh"]
