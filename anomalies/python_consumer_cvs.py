from kinesis.consumer import KinesisConsumer

import sys
import logging

logging.basicConfig()
logger = logging.getLogger('logger')
#logger.warning('this is a log message')

the_file = open("/tmp/data_from_stream.txt", "a+")

nr_columns_in_row = 3
nr_counter = 1

consumer = KinesisConsumer(stream_name=str(sys.argv[1]))
for message in consumer:
    print "Received message: {0}".format(message)
    print(type(message))
    print "--- this is a dict, so I should be able to access it like message[\"Data\"]"
    print(message["Data"])
    print "Writing to file /tmp/data_from_stream.txt"
    if nr_counter < nr_columns_in_row:
        the_file.write(message["Data"].rstrip() + ',')
        nr_counter += 1
    else:
        the_file.write(message["Data"].rstrip() + '\n')
        nr_counter = 1
        the_file.flush()


the_file.close()
