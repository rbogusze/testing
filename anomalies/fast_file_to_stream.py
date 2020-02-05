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
    buffer_size_limit=100000,
    buffer_time_limit=0.2,
    kinesis_concurrency=1,
    kinesis_max_retries=10,
    record_delimiter='\n',
    stream_name='anomaly_output_stream',
    )

k = KinesisProducer(config=config)

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
  
file1.close() 

k.close()
k.join()
