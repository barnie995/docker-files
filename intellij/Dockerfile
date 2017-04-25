FROM debian:jessie

RUN \
  echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list && \
  apt-get update && \
  apt-get -t jessie-backports install -y openjdk-8-jdk

COPY ideaIU-*.tar.gz /opt/ideaIU.tar.gz

WORKDIR /opt/

RUN \
    tar -xvf ideaIU.tar.gz

WORKDIR /opt/idea-IU-171.3780.107/bin 
ENTRYPOINT ["./idea.sh"]
