"""

"""
dict_hobbies = {
    "qtx": ["看书", "编码", "旅游"],
    "lzmly": ["刷抖音", "看电影"],
    "于谦": ["抽烟", "喝酒", "烫头"]
}
# 打印"于谦"的第二个爱好
print(dict_hobbies["于谦"][1])
print(dict_hobbies["于谦"][1])
# 打印qtx所有爱好(一行一个)
for hobbies in dict_hobbies["qtx"]:
    print(hobbies)

for hobbie in dict_hobbies["qtx"]:
    print(hobbie)
# 打印lzmly的爱好数量
count = 0
for hobbies in dict_hobbies["lzmly"]:
    count += 1
print(count)

print(len(dict_hobbies["lzmly"]))
# 打印所有人的所有爱好(一行一个)
for hobbies in dict_hobbies.values():
    for hobbie in hobbies:
        print(hobbie)

for hobbies in dict_hobbies.values():
    for hobbie in hobbies:
        print(hobbie)
