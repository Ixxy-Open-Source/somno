FROM ubuntu:bionic

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    git less nano curl \
    ca-certificates \
    wget build-essential\
    # python basic libs
    python3.6 python3.6-dev python3.6-venv gettext python3-distutils \
    # postgresql
    libpq-dev postgresql-client && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*

# install pip
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py && rm get-pip.py
RUN pip3 install --no-cache-dir setuptools wheel -U

CMD ["/bin/bash"]

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN export LC_ALL=en_US.UTF-8
RUN export LANG=en_US.UTF-8
RUN locale-gen en_US.UTF-8

RUN mkdir -p /data/web

WORKDIR /data/web

RUN mkdir -p ./somno_app/statics/admin

COPY requirements.txt /data/web/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /data/web/