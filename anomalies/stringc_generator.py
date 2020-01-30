
count = 0
max_count = 100

one_line = ""

while True: 
    if count > max_count: 
        break

    print("   \"column{}\"        DOUBLE,".format(count)) 
    count += 1 
    one_line = one_line + "\"COL" + str(count) + "\", "

print (one_line)
  
