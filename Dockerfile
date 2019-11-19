FROM python:3.7.4-alpine3.10

WORKDIR /app

COPY . /app

RUN apk add --no-cache bash

RUN apk add binutils libc-dev

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache postgresql-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers
RUN pip3 install pip --upgrade
RUN pip3 install -r requirements.txt
RUN apk del .build-deps
