#!/bin/bash

while [ 1 ]
do
  EPOCH_NOW=`date +%s`
  # introduce some anomaly
  if ! (($EPOCH_NOW % 45)); then
    #echo "divisible by 4."
    echo "$EPOCH_NOW 10 15 18" 
  else
    echo "$EPOCH_NOW 1 2 3" 
  fi
  sleep 1
done
