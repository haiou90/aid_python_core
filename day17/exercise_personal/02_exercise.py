list01 = [1,3,8,12,20,28,35]
list_result = []
for item in list01:
    list_result.append(item ** 2)

print(list_result)

list_result = [item ** 2 for item in list01]
print(list_result)

list_result =(item ** 2 for item in list01)
for item in list_result:
    print(item)


list_result = [item for item in list01 if item > 10]
print(list_result)


def generator():
    for item in list01:
        yield item
list_result= generator()

# list_result =(item for item in list01 if item > 10)
for item in list_result:
    print(item)