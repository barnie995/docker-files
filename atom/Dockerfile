# Base docker image
FROM debian:stretch
LABEL maintainer "Jessie Frazelle <jess@linux.com>"

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    gconf2 \
    gconf-service \
    gvfs-bin \
    libasound2 \
    libcap2 \
    libgconf-2-4 \
    libgnome-keyring-dev \
    libgtk2.0-0 \
    libnotify4 \
    libnss3 \
    libxkbfile1 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*


# copy the source

COPY atom*.deb /tmp/atom.deb

RUN dpkg -i /tmp/atom.deb

# Autorun atom
ENTRYPOINT [ "atom", "--foreground" ]
