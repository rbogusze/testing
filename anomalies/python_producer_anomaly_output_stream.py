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
    stream_name='anomaly_output_stream',
    )

k = KinesisProducer(config=config)

# read from file
file1 = open('/home/ec2-user/anomaly_output_stream.txt', 'r') 
count = 0

while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 

    # send it to Kinesis
    k.send(line.strip())

    time.sleep(0.3)
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print("Line{}: {}".format(count, line.strip())) 
    #break
  
file1.close() 

k.close()
k.join()
