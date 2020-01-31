from kinesis.consumer import KinesisConsumer

import sys
import logging
import json
import re

logging.basicConfig()
logger = logging.getLogger('logger')
#logger.warning('this is a log message')

consumer = KinesisConsumer(stream_name=str(sys.argv[1]))
for message in consumer:
    print "Received message: {0}".format(message)
    # filter out the datetime.datetime
    print(message)
    message_re = re.sub('u.*tzinfo\=tzlocal\(\)\)\,', '', str(message))
    print("-------")
    print(message_re)
    
    json_string = json.dumps(message_re)
    print(json_string)
    #jdata = json.loads(json_string)
    jdata = json.loads(message_re)
    print(jdata)
    print("-------omg")
    print(jdata["Data"])


