FROM debian:stretch

RUN \
    apt-get update && \
    apt-get -y install python3 python3-pip

RUN pip3 install hashid

ENTRYPOINT ["hashid"]
       
