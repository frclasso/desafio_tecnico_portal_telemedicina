FROM python:3.7-alpine
MAINTAINER Fabio Reis Classo

ENV PYTHONUNBEFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt

RUN  pip install -r /requirements.txt

RUN mkdir /config
WORKDIR /config
COPY ./app /config

RUN adduser -D user

USER user