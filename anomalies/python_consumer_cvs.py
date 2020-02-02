from kinesis.consumer import KinesisConsumer

import sys
import logging

logging.basicConfig()
logger = logging.getLogger('logger')
#logger.warning('this is a log message')

the_file = open("/tmp/data_from_stream.txt", "a+")

consumer = KinesisConsumer(stream_name=str(sys.argv[1]))
for message in consumer:
    print "Received message: {0}".format(message)
    print(type(message))
    print "--- this is a dict, so I should be able to access it like message[\"Data\"]"
    print(message["Data"])
    print "Writing to file /tmp/data_from_stream.txt"
    the_file.write(message["Data"] + '\n')


the_file.close()
