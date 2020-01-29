from kinesis.consumer import KinesisConsumer

import logging
logging.basicConfig()
logger = logging.getLogger('logger')
logger.warning('this is a log message')

consumer = KinesisConsumer(stream_name='remi_data_stream')
for message in consumer:
    print "Received message: {0}".format(message)
