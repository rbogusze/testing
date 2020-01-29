from kinesis_producer import KinesisProducer

import time
import logging
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
    stream_name='remi_data_stream',
    )

k = KinesisProducer(config=config)

# read from array
#records = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#for record in records:
#    k.send(record)

# read from file
file1 = open('/var/log/readings.txt', 'r') 
count = 0

while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 
    
    # send it to Kinesis
    k.send(line)

    time.sleep(1)
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    #print("Line{}: {}".format(count, line.strip())) 
    print("Line{}: {}".format(count, line)) 
  
file1.close() 

k.close()
k.join()
