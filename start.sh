#!/bin/bash
set -e
echo "Starting"

export DOCKERHOST=`/sbin/ip route|awk '/default/ { print $3 }'`
echo "Docker Host: " $DOCKERHOST
