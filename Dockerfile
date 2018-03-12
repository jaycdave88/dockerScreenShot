FROM ubuntu:16.04

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential xorg libssl-dev libxrender-dev wget

RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz

ADD ./start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]