#!/usr/bin/env python

# https://pypi.org/project/kinesis-python/

from kinesis.consumer import KinesisConsumer

import sys
import logging
logging.basicConfig()
logger = logging.getLogger('logger')
logger.warning('this is a log message')

consumer = KinesisConsumer(stream_name=str(sys.argv[1]))

size_treshold = float(sys.argv[2])
sum_treshold = float(sys.argv[3])

print "Received size_treshold: {0}, sum_treshold: {1}".format(size_treshold,sum_treshold)

message_count = 1
size_sum = 0
size_count = 0
sum_sum = 0
anomaly_list = []

for message in consumer:
    #print "Received message: {0}".format(message)
    print (message["Data"])
    string = message["Data"]
    commacount = string.count(',')
    endlinecount = string.count('\n')
    print "Message: {0}, comma count: {1} endline count: {2}".format(message_count,commacount,endlinecount)
    message_count += 1 

    # Now treat it like numbers, I assume that each data field can contain anomaly scores delimited by \n or ,
    data_string = message["Data"].replace(',', '\n')
    readings = data_string.split("\n")
    # Remove empty strings from a list of strings
    readings = filter(None, readings)

    for current_reading in readings:
        current_reading = float(current_reading)
        print "Current reading: {0}".format(current_reading)
        print "List has size of: {0}".format(len(anomaly_list))
        if len(anomaly_list) > size_treshold:
            print "Removing element from the beggining of the list list"
            anomaly_list.pop(0)
        print "Add element to the list"
        anomaly_list.append(current_reading)
        anomaly_list_sum = sum(anomaly_list)
        print "Sum of the elements in the list: {0}".format(anomaly_list_sum)
        if anomaly_list_sum > sum_treshold:
            print "WULF"
            print "WULF"
            print "WULF"

    

