#!/bin/bash

aws kinesis list-streams > /tmp/list-streams.txt
cat /tmp/list-streams.txt | grep "anomaly_input_stream" | tr -d " " | tr -d "\"" | tr -d "," > /tmp/list-streams-filtered.txt

while read LINE
do
  echo "Deleting $LINE"
  aws kinesis delete-stream --stream-name $LINE

done < /tmp/list-streams-filtered.txt
