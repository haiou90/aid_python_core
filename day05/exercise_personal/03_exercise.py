list_region = ["香港", "内蒙古", "四川"]
list_add = [6, 0, 0]
list_existing = [51, 25, 16]

print(list_region[1:2])  # print(list_region[len(list_region//2)])
print(list_add[:2])
print(list_add[1:])

list_region[2] = "sc"
print(list_region)

list_add[:2] = [0, 0]
print(list_add)

list_existing[1:] = [26, 17]
print(list_existing)

list_existing[1:1] = [26, 17]
print(list_existing)
