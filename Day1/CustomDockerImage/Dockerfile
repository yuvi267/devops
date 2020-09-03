FROM ubuntu:16.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org>

RUN apt update  && apt install -y default-jdk maven git openssh-server sudo

RUN useradd -m -p password -s /bin/bash devops
RUN echo "devops:devops" | chpasswd

RUN chown -R devops /home/devops

RUN mkdir -p /var/run/sshd
RUN chmod 755 /var/run/sshd

COPY sudoers /etc/sudoers


CMD ["/usr/sbin/sshd", "-D"]
