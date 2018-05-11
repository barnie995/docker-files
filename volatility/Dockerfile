FROM debian:jessie

RUN \
    apt-get update && \
    apt-get -y install python2.7 git

WORKDIR /opt/

RUN \
    git clone https://github.com/volatilityfoundation/volatility.git && \
    chmod -R 777 volatility/

WORKDIR /opt/volatility/

ENTRYPOINT ["bash"]
