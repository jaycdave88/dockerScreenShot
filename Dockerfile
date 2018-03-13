FROM ubuntu:14.04

RUN apt-get update -y && apt-get -y install python-qt4 libqt4-webkit xvfb python-pip && pip install webkit2png

ADD ./start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/usr/bin/python2.7"]