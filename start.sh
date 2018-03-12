#!/bin/bash
set -e
echo "Starting"

export DOCKERHOST=`/sbin/ip route|awk '/default/ { print $3 }'`
echo "Docker Host: " $DOCKERHOST

start="$@"

port=$(env | grep _TCP_PORT | cut -d = -f 2)

echo -n "waiting for TCP connection to $host:$port..."

while ! nc -w 1 $DOCKERHOST $port 2>/dev/null
do
  echo -n .
  sleep 1
done

final=${start/dockerhost/$DOCKERHOST}

/wkhtmltox/bin/wkhtmltoimage ${final}