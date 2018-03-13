#!/bin/bash
set -e
echo "Starting"

export DOCKERHOST=`/sbin/ip route|awk '/default/ { print $3 }'`
echo "Docker Host: " $DOCKERHOST

start="$@"

port=$(env | grep _TCP_PORT | cut -d = -f 2)

sleep 10

final=${start/dockerhost/$DOCKERHOST}

/wkhtmltox/bin/wkhtmltoimage ${final}