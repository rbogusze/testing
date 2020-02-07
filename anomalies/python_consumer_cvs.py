from kinesis.consumer import KinesisConsumer

import sys
import logging
import time

logging.basicConfig()
logger = logging.getLogger('logger')
#logger.warning('this is a log message')

the_file = open("/tmp/data_from_stream.txt", "a+")

nr_columns_in_row = 30
nr_counter = 1

consumer = KinesisConsumer(stream_name=str(sys.argv[1]))
for message in consumer:
    print "Received message: {0}".format(message)
    print(type(message))
    print "--- this is a dict, so I should be able to access it like message[\"Data\"]"
    print(message["Data"])

    # Now I need to loop through the Data block before I request another one
    # split the string on \n char and loop through elements
    print "what is that:"
    readings = message["Data"].split("\n")
    # Remove empty strings from a list of strings
    readings = filter(None, readings)

    for current_reading in readings:
        print "Current reading: {0}".format(current_reading)

        if nr_counter < nr_columns_in_row:
            the_file.write(current_reading.rstrip() + ',')
            nr_counter += 1
        else:
            the_file.write(current_reading.rstrip() + '\n')
            nr_counter = 1
            print "flush writing to file /tmp/data_from_stream.txt"
            the_file.flush()
            #time.sleep(1)


the_file.close()
