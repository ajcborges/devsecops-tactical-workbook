# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye 

LABEL maintainer="Kevin Flynn <Creator4983@encom.com>" 

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /workspace
ENV MY_DIR /workspace
ADD . ${MY_DIR}

RUN apt-get update && \
    apt-get -y install apt-utils

