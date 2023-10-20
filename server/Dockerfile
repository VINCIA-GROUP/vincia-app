FROM python:3.9.18-alpine3.18 AS base

WORKDIR /app

COPY . /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

EXPOSE 8080

CMD ["python3", "run.py"]