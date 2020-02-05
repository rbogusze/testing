#!/usr/bin/env python

from kinesis.consumer import KinesisConsumer

import sys
import logging
import time

logging.basicConfig()
logger = logging.getLogger('logger')

the_file = open(str(sys.argv[2]), "a+")

consumer = KinesisConsumer(stream_name=str(sys.argv[1]))
for message in consumer:
    print "Received message: {0}".format(message)
    print(type(message))
    print "--- this is a dict, so I should be able to access it like message[\"Data\"]"
    #print(message["Data"])
    sys.stdout.write(message["Data"])

    # Remove empty strings from a list of strings

    the_file.write(message["Data"])
    the_file.flush()


the_file.close()
