FROM python:3.11.0-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./installer/requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip && pip install -r /tmp/requirements.txt
COPY . /app
EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "main:app" ]