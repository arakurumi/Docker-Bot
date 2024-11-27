FROM arakurumi/mltb:latest

COPY . .

RUN python -m venv --system-site-packages mltb

RUN mltb/bin/pip install --no-cache-dir --requirement requirements.txt