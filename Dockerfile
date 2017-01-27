FROM ubuntu:16.04
MAINTAINER "John Hazelwood" <jhazelwo@users.noreply.github.com>
RUN apt-get clean && \
  apt-get -y update && \
  apt-get -y upgrade && \
  apt-get -y install curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /var/cache/*
RUN install -d -m 0700 -o 1000 -g 1000 /home/human && \
  groupadd --gid 1000 human && \
  useradd --uid 1000 --gid 1000 --home-dir /home/human -M --shell /bin/bash human
USER human
ENTRYPOINT ["/bin/bash", "--login"]
