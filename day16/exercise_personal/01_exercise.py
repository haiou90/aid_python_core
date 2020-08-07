message =(1,2,3,4)
iterator= message.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

message ={1:"a",2:"b",3:"c",4:"d"}
iterator= message.values().__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

message ={1:"a",2:"b",3:"c",4:"d"}
iterator= message.__iter__()
while True:
    try:
        key = iterator.__next__()
        value = message[key]
        print(key,value)
    except StopIteration:
        break
















message = (1,2)
a= message.__iter__()
while True:
    try:
        b= a.__next__()
        print(b)
    except StopIteration:
        break