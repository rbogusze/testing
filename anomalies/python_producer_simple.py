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
    stream_name='kinesis_input_stream_main',
    )

k = KinesisProducer(config=config)

# read from array
records = ["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9","2.0"]
#records = ["0.7216815647963053","0.7738460967569096","0.6662517246320603","0.5939564972919152","0.9970899642495911","0.6768665336144464","0.6404054932682939"]
#records = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
for record in records:
    k.send(record)
    #time.sleep(1)

time.sleep(1)

k.close()
k.join()
