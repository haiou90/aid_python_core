
# 打印"于谦"的第二个爱好
# 打印qtx所有爱好(一行一个)
# 打印lzmly的爱好数量
# 打印所有人的所有爱好(一行一个)
dict_hobbies = {
"qtx": ["看书", "编码", "旅游"],
"lzmly": ["刷抖音", "看电影"],
"于谦": ["抽烟", "喝酒", "烫头"]
}

# print(dict_hobbies["于谦"][1])
# for v in dict_hobbies["qtx"]:
#     print(v)
for i in range(len(dict_hobbies["qtx"])-1,-1,-1):
    print(dict_hobbies["qtx"][i])

# count = 0
# for v in dict_hobbies["lzmly"]:
#     count += 1
# print(count)
print(len(dict_hobbies["lzmly"]))

for k,v in dict_hobbies.items():
    print("%s的爱好有%s" %(k,v))
for hobbies in dict_hobbies.values():
    for hobbie in hobbies:
        print(hobbie)