#!/bin/bash

aws kinesisanalytics list-applications > /tmp/list-applications.txt
cat /tmp/list-applications.txt | grep "ApplicationName" | awk -F":" '{print $2}' | tr -d " " | tr -d "\"" | tr -d "," > /tmp/list-applications-filtered.txt

while read LINE
do
  echo $LINE
  aws kinesisanalytics describe-application --application-name $LINE >  /tmp/describe-application.txt
  V_CREATION_TIME=`cat /tmp/describe-application.txt | grep "CreateTimestamp" | awk -F":" '{print $2}' | tr -d " " | tr -d "\"" | tr -d ","`
  echo "V_CREATION_TIME: $V_CREATION_TIME"
  echo "Deleting $LINE with $V_CREATION_TIME"
  aws kinesisanalytics delete-application --application-name $LINE --create-timestamp $V_CREATION_TIME

done < /tmp/list-applications-filtered.txt
