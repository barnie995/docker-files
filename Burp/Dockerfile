FROM debian:jessie

# Install Java as a dependcy
RUN \
    echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get -t jessie-backports install -y openjdk-8-jdk

# Add Burp User and Group
RUN \
    groupadd --gid 995 burp && \
    useradd -m --uid 995 --gid 995 burp


# Copy the version of Burp in the folder to the machine
COPY burpsuite_free_*.jar /home/burp/opt/burpsuite.jar

# Change perms of the folder to burp user
RUN chown -R burp:burp /home/burp/opt/ && \
    chmod -R 700 /home/burp/opt/    

# Offer up port 8080 to the network
EXPOSE 8080:8080

# Switch user to burp
USER burp

# Change working directories
WORKDIR /home/burp/opt/

# When run, run the below command
ENTRYPOINT ["java", "-jar", "burpsuite.jar"]  

