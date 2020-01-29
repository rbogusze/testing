from kinesis_producer import KinesisProducer

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

records = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

for record in records:
    k.send(record)

k.close()
k.join()
