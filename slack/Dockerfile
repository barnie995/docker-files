FROM debian:stretch

#Dependicys for Slack
RUN \
    apt-get update && \
    apt-get -y install \    
    gconf2 \
    gconf-service \
    libgtk2.0-0 \
    libnotify4 \
    libxtst6 \
    libnss3 \
    python \
    gvfs-bin \
    xdg-utils \
    apt-transport-https \
    libxss1 \
    libgnome-keyring0 \
    gir1.2-gnomekeyring-1.0 \
    libappindicator1 \
    libasound2
    

COPY slack-desktop*.deb /tmp/slack/slack-desktop.deb

WORKDIR /tmp/slack/

RUN dpkg -i slack-desktop.deb




ENTRYPOINT ["/usr/lib/slack/slack"]
