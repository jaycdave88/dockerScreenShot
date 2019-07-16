FROM debian:stretch
#MAINTAINER Jay Davé <jay.dave@datadoghq.com>

RUN apt-get update -y && \
	apt-get -y install wkhtmltopdf-dbg && \
	apt-get -y install xvfb

RUN chmod 755 /usr/bin/wkhtmltopdf
RUN chmod 755 /usr/bin/wkhtmltoimage

COPY ./dd-email.py ./opt

CMD tail -f /dev/null