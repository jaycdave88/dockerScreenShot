#!/bin/bash
set -e
echo "Starting"

export DOCKERHOST=`/sbin/ip route|awk '/default/ { print $3 }'`
echo "Docker Host: " $DOCKERHOST

start="$@"

port=$(env | grep _TCP_PORT | cut -d = -f 2)

final=${start/dockerhost/$DOCKERHOST}

/usr/local/bin/webkit2png ${final}