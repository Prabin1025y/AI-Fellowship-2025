#!/usr/bin/env bash

# Usage: wait-for-it.sh host:port -- command to run

HOST_PORT="$1"
shift

HOST=$(echo $HOST_PORT | cut -d: -f1)
PORT=$(echo $HOST_PORT | cut -d: -f2)

until nc -z "$HOST" "$PORT"; do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

echo "$HOST:$PORT is up – running command"
exec "$@"
