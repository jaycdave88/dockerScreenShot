#!/bin/bash
set -e
echo "Starting"

export DOCKERHOST=`/sbin/ip route|awk '/default/ { print $3 }'`
echo "Docker Host: " $DOCKERHOST

start="$@"

port=$(env | grep _TCP_PORT | cut -d = -f 2)

sleep 30

final=${start/dockerhost/$DOCKERHOST}

/wkhtmltox/bin/wkhtmltoimage ${final}