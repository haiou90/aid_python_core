"""列表适合：存储单一维度的信息
疫情地区列表（地区）
字典适合：存储多个维度的信息
疫情信息(地区、新增人数、现有人数..)

练习1: 创建三个字典, 存储前三个地区疫情信息(地区, 新增, 现有, 累计, 治愈)
练习2: 为以上三个字典, 添加si亡信息
练习3: 删除第一个字典的新增人数,
练习4: 将第二个字典的新增人数设置为0,
练习5: 打印第三个字典信息:
格式: xx新增xx, 现有xx, 累计xx, 治愈xx, si亡xx
"""
dict_epidemic_of_hongkong = {"region": "香港", "add": 6, "remain": 53, "summary": 1099, "cured": 1042}
dict_epidemic_of_mongolia = {"region": "内蒙古", "add": 0, "remain": 21, "summary": 235, "cured": 213}
dict_epidemic_of_sichuan = {"region": "四川", "add": 1, "remain": 17, "summary": 578, "cured": 558}

if "dead" not in dict_epidemic_of_hongkong:
    dict_epidemic_of_hongkong["dead"] = 4
if "dead" not in dict_epidemic_of_mongolia:
    dict_epidemic_of_mongolia["dead"] = 1
if "dead" not in dict_epidemic_of_sichuan:
    dict_epidemic_of_sichuan["dead"] = 3

del dict_epidemic_of_hongkong["add"]

if "add" in dict_epidemic_of_mongolia:
    dict_epidemic_of_mongolia["add"] = 0
for key, value in dict_epidemic_of_sichuan.items():
    print(key)
    print(value)

print("%d新增%d, 现有%d, 累计%d, 治愈%d, 死亡%d"
      % (dict_epidemic_of_sichuan["region"],
         dict_epidemic_of_sichuan))
