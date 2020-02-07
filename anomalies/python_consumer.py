# https://pypi.org/project/kinesis-python/

from kinesis.consumer import KinesisConsumer

import sys
import logging
logging.basicConfig()
logger = logging.getLogger('logger')
logger.warning('this is a log message')

#consumer = KinesisConsumer(stream_name='remi_data_stream')
#consumer = KinesisConsumer(stream_name='remi_data_anomalies')
consumer = KinesisConsumer(stream_name=str(sys.argv[1]))

print(dir(consumer))

message_count = 1
for message in consumer:
    #print "Received message: {0}".format(message)
    #print (message["Data"])
    string = message["Data"]
    lst = string.split(",")
    stringcount = len(lst)
    commacount = string.count(',')
    endlinecount = string.count('\n')
    print "Message: {0}, there are: {1} elements in one message; comma count: {2} endline count: {3}".format(message_count,stringcount,commacount,endlinecount)
    message_count += 1 

