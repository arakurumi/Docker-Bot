FROM arakurumi/mltb:latest

RUN python -m venv --system-site-packages mltb

COPY . .

RUN mltb/bin/pip install --no-cache-dir --requirement requirements.txt