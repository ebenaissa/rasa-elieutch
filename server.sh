#!/bin/sh

if [ -z "$PORT"]
then
  PORT=5005
fi

# Start actions server in background
rasa run actions --actions actions&

# Start rasa server
rasa run --enable-api --port $PORT