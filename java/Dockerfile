FROM debian:jessie

RUN \
  echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list && \
  apt-get update && \
  apt-get -t jessie-backports install -y openjdk-8-jdk

EXPOSE 6789

ENTRYPOINT ["bash"]
