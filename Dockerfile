FROM scratch
MAINTAINER Jay Dave <jay.dave@datadoghq.com>

RUN apt-get update && apt-get install -y \
	wkhtmltopdf-dbg \
	xvfb-run

ENTRYPOINT ['/usr/bin/xvfb-run --server-args="-screen 0, 1920x1080x24"']