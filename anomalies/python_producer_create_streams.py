from kinesis_producer import KinesisProducer

import time
import os
import logging
logging.basicConfig()
logger = logging.getLogger('logger')
#logger.warning('this is a log message')

# global variables
nr_streams = 50

#-------------------
# First I need to be able to create a Kinesis Data Stream from API

def create_kinesis_data_stream(stream_name):
    print(stream_name)
    os.system("aws kinesis create-stream --stream-name " + stream_name + " --shard-count 1 --region eu-west-1")
    os.system("aws kinesis add-tags-to-stream --stream-name " + stream_name + " --tags Responsible=Sokalszczuk,Project=SPM,Interesting=how_much_it_costs")

def create_kinesis_analytics(analytics_name, stream_name):
    print(stream_name)
    # prepare template
    os.system("cat create-application.json | sed -e 's/ala_ma_kota/" + stream_name + "/' | sed -e 's/cadabra1/"+ analytics_name + "/' > trash_template.json")
    os.system("aws kinesisanalytics create-application --cli-input-json file://trash_template.json")
    os.system("aws kinesisanalytics start-application --application-name " + analytics_name + " --input-configurations Id=1.1,InputStartingPositionConfiguration={InputStartingPosition=NOW}")
    

def push_data_to_stream(sname, stream_data):
    print("Pushing data to: {}".format(sname))
    config = dict(
        aws_region='eu-west-1',
        buffer_size_limit=100000,
        buffer_time_limit=0.2,
        kinesis_concurrency=1,
        kinesis_max_retries=10,
        record_delimiter='\n',
        stream_name=sname,
    )

    #print(config)

    k = KinesisProducer(config=config)
    k.send(stream_data)
    k.close()
    k.join()


# tmp
#small_line = "ala ma kota a kot ma ale"     
#push_data_to_stream("anomaly_input_stream0",small_line)
#exit()

# declare a list that will store streams
nr_stream = 0
name_stream = ""
for nr_stream in range(0,nr_streams):
    name_stream = ("anomaly_input_stream" + str(nr_stream))
    name_analytics = ("anomaly_analytics" + str(nr_stream))
    print("Creating Kinesis stream: {}".format(name_stream))
    create_kinesis_data_stream(name_stream)
    print("Creating Kinesis analytics for: {}".format(name_analytics))
    create_kinesis_analytics(name_analytics, name_stream)

print("Creating Kinesis stream: anomaly_output_stream")
create_kinesis_data_stream("anomaly_output_stream")

#exit()
#------------------

# read from array
#records = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#for record in records:
#    k.send(record)

# read from file
file1 = open('/home/ec2-user/result.csv', 'r') 
count = 0

while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 

    # replace comma ',' with space ' '
    # line = line.replace(",", " ")

    # looks like there are too many columns, I need to be able to select only handful of them
    line_split = line.split(",")

    columns_interesting = 30
    wcount = 0
    nr_stream = 0
    name_stream = ""
    for nr_stream in range(0,nr_streams):
        #print(nr_stream, nr_streams)
        #print("Working for: {}".format(nr_stream))
        name_stream = ("anomaly_input_stream" + str(nr_stream))
        small_line = ""
        while wcount < columns_interesting:
            small_line = small_line + "," + line_split[wcount]
            wcount += 1

        # remove first comma
        small_line = small_line[1:]
        #print(small_line)
    
        # send it to Kinesis
        push_data_to_stream(name_stream,small_line)
        #print("Variables after the push")
        #print(wcount,columns_interesting)
        columns_interesting += 30

    #print("User exit")
    #exit()

    #time.sleep(1)
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    #print("Line{}: {}".format(count, line.strip())) 
    #print("Line{}: {}".format(count, line)) 
    #print("Line{}: {}".format(count, small_line)) 
    print("Sending line {}".format(count)) 
    #break
  
file1.close() 

