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
    print (message["Data"])
    string = message["Data"]
    commacount = string.count(',')
    endlinecount = string.count('\n')
    print "Message: {0}, comma count: {1} endline count: {2}".format(message_count,commacount,endlinecount)
    message_count += 1 

