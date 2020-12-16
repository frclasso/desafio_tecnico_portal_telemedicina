FROM python:3.7-alpine
MAINTAINER Fabio Reis Classo

ENV PYTHONUNBEFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /config
WORKDIR /config
COPY ./app /config

RUN adduser -D user

USER user