FROM debian:stretch
MAINTAINER Jay Davé <jay.dave@datadoghq.com>

RUN apt-get update -y
RUN apt-get -y install python3
RUN apt-get -y install wkhtmltopdf-dbg 
RUN apt-get -y install xvfb

RUN chmod 755 /usr/bin/wkhtmltopdf
RUN chmod 755 /usr/bin/wkhtmltoimage

# Add start script
ADD start.sh /usr/bin/start.sh
RUN chmod 755 /usr/bin/start.sh

# Add python script
#ADD dd-email.py /usr/bin/dd-email.py
#RUN chmod 755 /usr/bin/dd-email.py

# Execute start script to keep container running
#CMD [ "/usr/bin/start.sh" ]