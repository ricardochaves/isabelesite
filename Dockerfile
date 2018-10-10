FROM python:3.6.2rc2

LABEL maintainer "ricardo.chaves@infoglobo.com.br"

RUN mkdir /base_site
WORKDIR /base_site

ADD . /base_site

RUN chmod +x ./base_site.sh && \
    apt-get install libmysqlclient-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements_dev.txt
