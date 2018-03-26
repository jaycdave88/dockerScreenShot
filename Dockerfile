FROM debian

RUN apt-get update -y
RUN apt-get -y install wkhtmltopdf-dbg
RUN apt-get -y install xvfb

RUN su root

RUN /usr/bin/xvfb-run -a /usr/bin/wkhtmltoimage --javascript-delay 20000 https://p.datadoghq.com/sb/rklUvX-4e920a9b3350900a4d4344c17384d761 google.png