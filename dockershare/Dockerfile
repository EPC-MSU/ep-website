# Docker container for SSHFS access to server "download" directory

# Use the same platform as the main container
FROM python:3.7-slim-buster

RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    mkdir /root/.ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY authorized_keys /root/.ssh/

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
