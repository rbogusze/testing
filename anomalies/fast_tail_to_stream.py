#!/usr/bin/env python

from kinesis_producer import KinesisProducer

import time
import logging
import sys
import subprocess
import select

logging.basicConfig()
logger = logging.getLogger('logger')
logger.warning('this is a log message')

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

f = subprocess.Popen(['tail','-F',str(sys.argv[1])],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(1):
        line = f.stdout.readline() 
        print line
        # send it to Kinesis
        k.send(line)
    time.sleep(1)



  
f.close() 

k.close()
k.join()
