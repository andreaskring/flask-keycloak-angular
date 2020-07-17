FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN groupadd -g 73001 --system flask
RUN useradd -u 73001 -g flask --system flask

WORKDIR /app

#USER flask

COPY ./flask-app/* ./

RUN pip install -r requirements.txt

USER flask
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "--threads", "4", "--worker-class", "gthread", "--worker-tmp-dir", "/dev/shm", "--log-file", "-", "app:app"]
