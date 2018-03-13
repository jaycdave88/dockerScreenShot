# minmal Ubuntu 16.04
FROM phusion/baseimage:latest

# headless browser 
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential xorg libssl-dev libxrender-dev wget

# downloading and setting webkit2png file
RUN wget https://raw.github.com/paulhammond/webkit2png/master/webkit2png -P /usr/local/bin 

# giving permissions
RUN chmod a+x /usr/local/bin/webkit2png 

ADD ./start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]