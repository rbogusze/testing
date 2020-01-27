import time
import random

while True:
    with open("/tmp/data.txt", "a+") as the_file:
        the_file.write(str(random.uniform(1.0, 2.0)) + '\n')
        time.sleep(1)

