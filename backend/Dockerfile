FROM python:3.13-alpine

WORKDIR /app
COPY requirements.txt /app/

RUN python3 -m venv /app/venv

RUN /app/venv/bin/pip install --upgrade pip && \
   /app/venv/bin/pip install -r requirements.txt

COPY . /app/

CMD ["/app/venv/bin/python", "backend/etl/run_etl.py"]