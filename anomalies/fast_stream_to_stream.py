#!/usr/bin/env python

from kinesis_producer import KinesisProducer
from kinesis.consumer import KinesisConsumer

import sys
import logging
import time

logging.basicConfig()
logger = logging.getLogger('logger')

config = dict(
    aws_region='eu-west-1',
    buffer_size_limit=100000,
    buffer_time_limit=0.2,
    kinesis_concurrency=1,
    kinesis_max_retries=10,
    record_delimiter='',
    stream_name=str(sys.argv[2]),
    )

k = KinesisProducer(config=config)
consumer = KinesisConsumer(stream_name=str(sys.argv[1]))
nr_columns_in_row = 30
nr_counter = 1
line_to_send = ""
for message in consumer:
    print "Received message: {0}".format(message)
    print(type(message))
    # this is a dict, so I should be able to access it like message[\"Data\"]
    line = message["Data"]
    sys.stdout.write(line)
    #----
    # first replace the end line characters into comma as multiple lines can be placed in the same Data block
    line = line.replace("\n", ",")
    print(line)

    # then split it into desired nr of columns and end with end line character
    readings = line.split(",")
    # Remove empty strings from a list of strings
    readings = filter(None, readings)

    for current_reading in readings:
        print "Current reading: {0}".format(current_reading)

        if nr_counter < nr_columns_in_row:
            line_to_send = line_to_send + current_reading + ','
            nr_counter += 1
        else:
            line_to_send = line_to_send + current_reading + '\n'
            nr_counter = 1
            print "sending to " + str(sys.argv[2]) + ":" + str(line_to_send)
            k.send(line_to_send)
            line_to_send = ""

k.close()
k.join()
