FROM python:3-alpine3.17 AS base

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 4000

ENTRYPOINT python ./application/app.py 
