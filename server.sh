#!/bin/sh

if [ -z "$PORT"]
then
  PORT=5005
fi

# Start actions server in background
rasa run actions --actions actions --debug

# Start rasa server
rasa run --enable-api --port $PORT