# syntax=docker/dockerfile:1

FROM 3.10-slim-bullseye 

LABEL maintainer="Kevin Flynn <Creator4983@encom.com>" \ 
      org.opencontainers.image.source="https://github.com/devsecfranklin/devsecops-tactical-workbook" 

ENV DEBIAN_FRONTEND noninteractive

COPY . /project
WORKDIR /project

RUN apt-get update && \
    apt-get -y install apt-utils

