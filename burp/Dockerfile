FROM debian:jessie

# Install Java as a dependcy
RUN \
    echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get -t jessie-backports install -y openjdk-8-jdk

# Copy the version of Burp in the folder to the machine
COPY burpsuite_free_*.jar /opt/burpsuite.jar

# Offer up port 8080 to the network
EXPOSE 8080

# Change working directories
WORKDIR /opt/

# When run, run the below command
ENTRYPOINT ["java", "-jar", "burpsuite.jar"]  

