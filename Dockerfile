FROM python:3.6
MAINTAINER Kevin <kevinliang188@hotmail.com>
RUN echo 'alias ll="ls -la"' > /root/.bashrc &&\
    echo 'export COVERAGE_SHOW_SUMMARY=1' >> ~/.bashrc
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip \
  && apt-get update -y \
  && apt-get autoremove -y \
  && apt-get install \
        vim \
        unoconv \
        imagemagick \
        ghostscript \
        freetds-dev \
        libgeos-dev \
        postgresql-client \
        xmlsec1 \
        build-essential \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev \
        shared-mime-info \
        -y

COPY . /usr/src/app
RUN pip install -r requirements-dev.txt && mkdir /var/log/realinvest
