# Run wireshark in a container
#
# docker run -d \
#   -v /etc/localtime:/etc/localtime:ro \
#   -v /tmp/.X11-unix:/tmp/.X11-unix \
#   -e DISPLAY=unix$DISPLAY \
#   --name wireshark \
#   jess/wireshark
#
FROM ubuntu:16.04
LABEL maintainer "Jessie Frazelle <jess@linux.com>"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    software-properties-common \
    --no-install-recommends && \
    add-apt-repository ppa:wireshark-dev/stable && \
    apt-get update && \
    apt-get install -y \
    wireshark \
    && rm -rf /var/lib/apt/lists/*


ENTRYPOINT  [ "wireshark" ]
