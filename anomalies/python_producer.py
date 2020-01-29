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
file1 = open('/home/ec2-user/result.csv', 'r') 
count = 0

while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 

    # replace comma ',' with space ' '
    # line = line.replace(",", " ")

    # looks like there are too many columns, I need to be able to select only handful of them
    line_split = line.split(",")

    columns_interesting = 10
    wcount = 0
    small_line = ""
    while wcount < columns_interesting:
        small_line = small_line + "," + line_split[count]
        wcount += 1

    # remove first comma
    small_line = small_line[1:]
    #print(small_line)
    
    # send it to Kinesis
    #k.send(line)
    k.send(small_line)

    time.sleep(1)
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    #print("Line{}: {}".format(count, line.strip())) 
    #print("Line{}: {}".format(count, line)) 
    #print("Line{}: {}".format(count, small_line)) 
    print("Sending line {}".format(count)) 
    #break
  
file1.close() 

k.close()
k.join()
