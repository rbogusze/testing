#!/usr/bin/env python

from kinesis_producer import KinesisProducer

import time
import logging
import sys

logging.basicConfig()
logger = logging.getLogger('logger')
logger.warning('this is a log message')

config = dict(
    aws_region='eu-west-1',
    buffer_size_limit=100,
    buffer_time_limit=0.2,
    kinesis_concurrency=1,
    kinesis_max_retries=10,
    record_delimiter='',
    stream_name=str(sys.argv[2]),
    )

k = KinesisProducer(config=config)

last_time_sleep = 0
record_count_before_sleep = 0

def every_x_seconds_sleep_for_y_seconds(x,y):
    epoch_time = int(time.time())
    print(epoch_time)
    global last_time_sleep
    if epoch_time - last_time_sleep > x:
        print "Time to sleep for {0}, as last Time I slept was {1} seconds ago".format(y,(epoch_time - last_time_sleep))
        print("Sleeping in every_x_seconds_sleep_for_y_seconds.")
        time.sleep(y)
        last_time_sleep = epoch_time

def every_x_records_sleep_for_y_seconds(x,y):
    global record_count_before_sleep
    record_count_before_sleep += 1
    if record_count_before_sleep > x:
        print "Time to sleep for {0}, as I processed {1} records already".format(y,record_count_before_sleep)
        print("Sleeping in every_x_records_sleep_for_y_seconds")
        time.sleep(y)
        record_count_before_sleep = 0


file1 = open(str(sys.argv[1]), 'r') 
count = 0

while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 


    # end of file is reached 
    if not line: 
        break

    print("Line{}: {}".format(count, line.strip())) 

    # send it to Kinesis
    k.send(line)

    #every_x_seconds_sleep_for_y_seconds(5,1)
    every_x_records_sleep_for_y_seconds(10,0.5)
    #print("Sleeping.")
    #time.sleep(0.9)
  
file1.close() 

k.close()
k.join()
