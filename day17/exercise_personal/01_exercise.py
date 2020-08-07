dict01 ={1:"a",2:"b",3:"c",4:"d",5:"d"}
for i,(k,v) in enumerate(dict01.items()):
    print(i,k,v)

for key,value in dict01.items():
    print(key,value)

for item in enumerate(dict01.items()):
    print(item)

list01 = [1,12,3,14,5,6]
for i,item in enumerate(list01):
    if item > 10:
        list01[i]= 0

print(list01)

list01 = [1,2,3,4]
list02 = [5,6,7,8]
list02 = [9,10,11,12]
list02 = [13,14,15,16]
list_taget =[[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]
list_taget_new = []
# for item in zip(list_taget[0],list_taget[1],list_taget[2],list_taget[3]):
#     list_taget_new.append(list(item))
#     print(list(item))

for item in zip(*list_taget):
    list_taget_new.append(list(item))
print(list_taget_new)