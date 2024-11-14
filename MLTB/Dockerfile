FROM arakurumi/mltb:latest

RUN python -m venv mltb

COPY . .

RUN mltb/bin/pip install --no-cache-dir --requirement requirements.txt