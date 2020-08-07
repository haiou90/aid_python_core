# exercise1
# print("你好,世界")
# usd = input("请输入美元:")
# rmb = float(usd) * 7.1465
# print(usd + "美元=" + str(rmb) + "人民币")

# exercise2
# print("你好")
# print("世界")
# name = input("请输入姓名:")
# print("您好:" + name)

# exercise3
# name01 得到的是数据("刘陈方")地址
# name01 = "刘陈方"
# print(name01)
# name02 = "闫艺锋"
# print(name02)
# name01 = "朱林旭"
# print("您好：" + name01)# 您好：朱林旭
# name03得到的是变量name02存储的数据("闫艺锋")地址
# name03 = name02
# print(name03)

# exercise4
# str_age = input("请输入你的年龄:")
# int_age = int(str_age) + 1
# print("明年你"+str(int_age))

# exercise5
# number01 = int("18")
# print(number01)
# number02 = int(18.5)
# print(number02)

# exercise6
# str01 = str(18)
# print(str01)
# str02 = str(18.5)
# print(str02)

# exercise7
# float01 = float(18)
# print(float01)
# float02 = float("18.5")
# print(float02)

# number03 = int("18我你") # 不像整数ValueError
# number03 = int("18.5") # 不像整数ValueError
# float03 = float("1.5a")

# exercise8
# number01 = 2
# number02 = 5
# print(number01 + number02)
# print(number02 ** number01)
# print(number02 / number01)
# print(number02 % number01)
# print(number02//number01)

# exercise9
# number01 = 2
# number01 += 5
# print(number01)

# exercise10
# print("$1398.00")
# print("Blue Yeti Studio电容麦克风 电脑USB网络 K歌录音YY直播话筒设备 麦克风单品")
# print("2条评价")
# print("数码专营店")

# exercise11
# subject = input("请输入I Kiss you 的主语:")
# predicate = input("请输入I Kiss you 的谓语:")
# object = input("请输入I Kiss you 的宾语:")
#
# print("您输入的是:")
# print("主语:" + subject + "谓语:" + predicate + "宾语:" + object)

# exercise12
# name_of_hubei_province = "湖北"
# print(name_of_hubei_province)
# name_of_hunan_province = "湖南"
# print(name_of_hunan_province)
# name_of_hunan_province = "湖南省"
# print(name_of_hunan_province)
# name_of_hunan_province = name_of_hubei_province
# print(name_of_hunan_province)

# exercise13
# name_of_beijing, region = "北京", "市"
# name_of_beijing_region = name_of_beijing + region
# region = "省"
# print(name_of_beijing_region)  # 北京市
# del name_of_beijing
# print(name_of_beijing_region)  # 北京市

# exercise14
# unit_price = float(input("请输入单价:"))
# amount = int(input("请输入购买数量:"))
# money = float(input("请输入支付金额:"))
# result = money - unit_price * amount
# print(result)

# exercise15
# diagnose = int(input("请输入确诊人数:"))
# cure_num = int(input("请输入治愈人数:"))
# print("治愈比例为:"+str(cure_num/diagnose*100)+"%")
# print("治愈比例为:%.2f" % float(cure_num/diagnose*100))
# print(f"治愈比例为:{cure_num/diagnose*100}%")   #百分比的输入

# exercise16
# amount = int(input("请输入两数:"))
# jin = amount // 16
# liang = amount % 16
# print(f"{jin}斤零{liang}两")

# exercise16
# bridegroom_name = "武大郎"
# bride_name = "潘金莲"
# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp
# print("交换后的新郎：" + bridegroom_name)  #
# print("交换后的新娘：" + bride_name)

# exercise17
# result = input("请输入您的职业:") == "总统"
# print(result)

# exercise18
# result = int(input("请输入你的财产:")) > 1000000 and input("请输入你是否有才华:") == "有"
# print(result)

# exercise19
# if input("请问您是否有才华：") == "有":
#     print("嫁给你")
# else:  # 互斥
#     print("拒绝你")

# exercise20
# number = int(input("请输入数字:"))
# if number > 0:
#     print("正数")
# elif number < 0:
#     print("负数")
# else:
#     print("零")

# exercise21
# result = bool("")
# print(result)
# result = bool(0)
# print(result)
# result = bool(None)
# print(result)
# result = bool(0.0)
# print(result)
# result = bool(1)
# print(result)
#
# message = input("请输入：")
# # if message != "": # 输入的不是空
# # if message != 0:
# if message:  # bool(message) 输入的有值
#     print("您输入的是:" + message)
# else:
#     print("您没有输入")

# exercise22
# if input("请输入性别:") == "男":
#     value = 1
# else:
#     value = 0

# value = 1 if input("请输入性别:") == "男" else 0
# print("性别编号：%s" % value)

# exercise23
# print(int(input("请输入年龄:")) > 25 and int(input("请输入身高:")) < 170)
# print(input("请输入职位:") == "高管" and int(input("请输入年薪:")) > 500000)
# print(int(input("请输入身高:")) > 180 and int(input("请输入年薪:")) > 100000 and int(input("请输入颜值:")) > 170)

# exercise24
# if int(input("请输入年龄：")) > 25 and float(input("请输入身高：")) < 170:
#     print("入职")
# else:
#     print("拒绝")
#
# if int(input("请输入身高")) > 180 and int(input("请输入财产:")) > 10000000 and int(input("请输入颜值:")) > 95:
#     print("闺女嫁给你")
# else:
#     print("去学习吧")

# exercise25
# 在终端中获取性别,
# 打印"您好先生" "您好女士" "性别未知"
# sex = input("请输入性别:")
# if sex == "男":
#     print("您好先生")
# elif sex == "女":
#     print("您好女士")
# else:
#     print("性别未知")

# exercise26
# price = float(input("请输入单价："))
# num = int(input("请输入数量："))
# money = float(input("请输入金额："))
# return_back = money - price * num
# if return_back > 0:
#     print("应找回%d元" % return_back)
# else:
#     print("金额不足")

# exercise27
# dict_course = {"1": "显示 Python语言核心编程",
#     2: "显示 Python高级软件技术",
#     3: "显示 Web 全栈",
#     4: "显示 网络爬虫",
#     5: "显示 数据分析、人工智能"}
# number = int(input("请输入课程阶段数："))
# print(dict_course[number])
# number = input("请输入课程阶段数：")
# print(dict_course[number])

# if number == "1":
#     print("Python语言核心编程")
# elif number == "2":
#     print("Python高级软件技术")
# elif number == "3":
#     print("Web全栈")
# elif number == "4":
#     print("网络爬虫")
# elif number == "5":
#     print("数据分析、人工智能")

# exercise28
# height1 = int(input("请输入身高："))
# height2 = int(input("请输入身高："))
# height3 = int(input("请输入身高："))
# height4 = int(input("请输入身高："))
# max_value = height1
#
# if max_value < height2:
#     max_value = height2
# if max_value < height3:
#     max_value = height3
# if max_value < height4:
#     max_value = height4
# print(max_value)

# exercise29
# ma = int(input("请输入你的心里年龄："))
# ca = int(input("请输入你的实际年龄："))
# iq = ma / ca * 100
# if iq >= 140:
#     print("天才")
# elif iq >= 120:
#     print("超常")
# elif iq >= 110:
#     print("聪慧")
# elif iq >= 90:
#     print("正常")
# elif iq >= 80:
#     print("迟钝")
# else:
#     print("低能")

# exercise30
# month = int(input("请输入月份:"))
# if month <= 0 or month >= 12:
#     print("输入的月份有误")
# else:
#     # 月份输入正确
#     if month == 2:
#         print("28天")
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         print("30天")
#     else:  # 1 3 5 7 8 10 12
#         print("31天")

# exercise31
# while True:
#     num = int(input("请输入电梯承载人数:"))
#     weight = float(input("请输入电梯承载重量:"))
#     if num < 10 and weight <= 1000:
#         print("电梯正常运行")
#     else:
#         print("超载")
#
#     if input("请输入q键退出:") == "q":
#         break

# exercise32
# count = 0
# sum_count = 0
# while count < 5:
#     count += 1
#     sum_count += count
# print(count)
# print(sum_count)

# exercise33
# import random
#
# number = random.randint(1,100)
# count = 0
# while count < 3:
#     guess = int(input("请猜数:"))
#     count += 1
#     if guess == number:
#         print("猜对了")
#         break
#     elif guess < number:
#         print("猜小了")
#         print("还有%d次机会" % (3-count))
#     else:
#         print("猜大了")
#         print("还有%d次机会" % (3 - count))
# else:
#     print("游戏失败")

# exercise34
# message = "我是齐天大圣"
# for item in message:
#     print(item)
#
# for item in "100":
#     print(item)

# exercise35
# for number in range(5):
#     print(number)

# exercise36
# sum_count = 0
# for count in range(1,101):
#     if count % 3 == 0:
#         sum_count += count
# print(sum_count)
#
# sum_count = 0
# for count in range(1,101):
#     if count % 3 != 0:
#         continue
#     sum_count += count  #类似于省略了else
# print(sum_count)

# exercise37
# \"  \'    换行\n   \\
# message = "我是\"孙悟空\"。"
# print(message)# 我是"孙悟空"。
#
# message = "我是\n孙悟空。"
# print(message)#
#
# url = "\a\b\c\d\e.txt"
# url = "\\a\\b\c\d\e.txt"
# # 原始字符：后面的字符串木有转义字符
# # url = r"\a\b\c\d\e.txt"
# print(url)

# exercise38
# while True:
#     state = "奇数" if int(input("请输入:")) % 2 == 1 else  "偶数"
#     print(state)
#     if input("请输入y继续:") != "y":
#         break

# exercise38
# sum_num = 0
# for num in range(4):
#     print(num, end=" ")
#
#     sum_num += num
# print()
# print(sum_num)
# sum_num = 0
# for num in range(2, 7):
#     print(num, end=" ")
#     sum_num += num
# print()
# print(sum_num)
# sum_num = 0
# for num in range(1, 8, 2):
#     print(num, end=" ")
#     sum_num += num
# print()
# print(sum_num)
# sum_num = 0
# for num in range(8, 3, -1):
#     print(num, end=" ")
#     sum_num += num
# print()
# print(sum_num)
# sum_num = 0
# for num in range(-1,-6, -1):
#     print(num, end=" ")
#     sum_num += num
# print()
# print(sum_num)

# exercise39
# thickness = 0.01 / 1000
# count = 0
# while thickness < 8848:
#     thickness *= 2
#     count += 1
# print(count)

# exercise40
# number = input("请输入一个整数:")
# sum_num = 0
# for item in number:
#     sum_num += int(item)
# print(sum_num)

# exercise41
# sum_value = 0
# for __ in range(5):
#     number = int(input("请输入一个整数:"))
#     sum_value += number
# print(sum_value)

# exercise42
# sum_value = 0
# while True:
#     number = input("请输入一个整数:")
#     if number == " ":
#         break
#     sum_value += int(number)
# print(sum_value)

# exercise42
# sum_value = 0
# for number in range(10,61):
#     unit = number % 10
#     if unit in [3, 5, 8]:
#         continue
#     sum_value += number
# print(sum_value)

# exercise43
# + 用于【拼接】两个容器
# name = "悟空"
# name += "八戒"
# print(name)  # "悟空八戒"
# # * 【重复】生成容器元素
# name *= 3
# print(name)
#
# # 比较 依次比较两个容器中元素,一但不同则返回比较结果。
# print("悟空" == "八戒")
# print("悟空" != "八戒")

# exercise44
# message = "我是花果山水帘洞美猴王齐天大圣"
# print(message[0])  # 打印第一个元素
# print(message[2])  # 打印第三个元素
# print(message[-2])  # 打印倒数第二个元素
# # print(message[100])# IndexError: string index out of range
# # print(message[-100])# IndexError: string index out of range
# print(message[-len(message)])  # 第一个
# print(message[len(message) - 1])  # 最后一个

# exercise45
# message = "我是花果山水帘洞美猴王齐天大圣"
# print(message[0:3:1])  # 我是花
# print(message[0:8:2])  # 我花山帘
# print(message[0:3])  # 我是花
# print(message[:3])  # 我是花
# print(message[:])  # 我是花果山水帘洞美猴王齐天大圣
# print(message[3:])  # 果山水帘洞美猴王齐天大圣
# print(message[3:-1])  # 果山水帘洞美猴王齐天大
# print(message[::-1])  #圣大天齐王猴美洞帘水山果花是我
# print(message[2:250])  # 花果山水帘洞美猴王齐天大圣
# print(message[2:7:-1])  #空
# print(message[7:2])  #空

# exercise46
# list_names = ["谭锦岳", "杨淮靖", "张昆鹏"]
# # list_names.remove("谭锦岳")
# print(list_names)
# del list_names[:]
# print(list_names)

# exercise47
list_names = ["谭锦岳", "杨淮靖", "张昆鹏", "佩琪"]
# for item in list_names:
#     print(item)
#     item = " "
#     print(item)
# print(list_names)

# for i in range(len(list_names)):
#     print(list_names[i])
# for i in range(len(list_names)-1, -1, -1):
#     print(list_names[i])

# exercise48
# list01 = [[10, 15], 20, 30]
# # 变量list02得到的是变量list01存储的列表地址
# list02 = list01
# # 变量list03得到的是新列表的地址
# list03 = list01[:]
# # 变量list04得到的是第一个列表的第一个元素记录的数据(10)地址
# list04 = list01[0]
# list01[0] = 100
# list03[1] = 1000
# # print(list01)
# # print(list02)
# # print(list03)
# # print(list04)
# import copy
# list01 = [10, [20, 30], [40, 50]]
# # list02 得到的是变量list01存储的列表地址
# list02 = list01
# # 通过list02修改列表第一个元素,再通过list01访问受影响
# list04 = copy.deepcopy(list01)
# list02[0] = "十"
# list02[1][0] = "二十"
# print(list01)
# print(list02)
# # list03 得到的列表浅拷贝(一层)出来的新列表
# list03 = list01[:]
# # 修改第一层(不影响拷贝前的数据list01)
# list03[0] = "a"
# print(list01)
# print(list02)
# print(list03)
# # 修改第二层(影响拷贝前的数据list01)
#
# list03[1][1] = "b"
# list04[0]= 100
# print(list01)
# print(list02)
# print(list03)
# print(list04)

# exercise49
# list_city = ["香港", "内蒙古", "四川"]
# list_new_people = [6, 0, 0]
# list_now_people = [51, 25, 16]
#
# list_names.append("台湾")
# list_new_people.append(3)
# list_now_people.append(5)
#
# list_city.insert(1,"广东")
# print(list_city)

# exercise50
# list_city = ["香港", "内蒙古", "四川"]
# list_new_people = [6, 0, 0]
# list_now_people = [51, 25, 16]
# for city in list_city:
#     print(city)
#
# for i in range(len(list_now_people)):
#     print(list_now_people[i])
# for i in range(len(list_now_people)-1,-1,-1):
#     print(list_now_people[i])
#
# del list_city[len(list_city)//2]
# del list_city[:2]
# del list_city[-2:-1]

# exercise51
# list_planet = ["水星", "金星", "huo星", "木星"]
# list_planet.insert(2,"地球")
# list_planet[4:] = ["土星","天王星","海王星"]
# print(list_planet[0])
# print(list_planet[-1])
# print(list_planet[:2])
# list_planet.remove("海王星")
# del list_planet[3]
# for i in range(len(list_planet)-1,-1,-1):
#     print(list_planet[i])
# exercise52
# list01 = ["北京", "上海"]
# list02 = list01
# list01[0] = "广州"
# list03 = list01[:]
# list03[-1] = "深圳"
# print(list01)  # ['广州', '上海']
# print(list02)
# print(list03)  # ['广州', '深圳']

# exercise53
# import copy
# list01 = ["北京",["上海","深圳"]]
# list02 = list01
# list03 = list01[:]
# list04 = copy.deepcopy(list01)
# list04[0] = "北京04"
# list04[1][1] = "深圳04"
# print(list04)
# print(list01) # ?
# list03[0] = "北京03"
# list03[1][1] = "深圳03"
# print(list01) # ?
# list02[0] = "北京02"
# list02[1][1] = "深圳02"
# print(list02) # ?
# print(list01)
# print(list03)

# exercise53
# list01 = ["孙悟空", "猪八戒", "唐僧"]
# result = "_".join(list01)
# print(result)
#
# result =""
# for number in range(10):
#     result += str(number)
# print(result)
#
# result = []
# for number in range(10):
#     result.append(str(number))
#     print(result)
# str_result = "".join(result)
# print(str_result)
#
# list_result = "孙悟空_猪八戒_唐僧".split("_")
# print(list_result)
#
# list01 = [34, 45, 5, 65, 76, 8]
# list_result = [number for number in list01 if number > 10]
# print(list_result)

# a, b = (80, 90)

# a, b = [80, 90]

# a, b = "悟空"
# print(a)
# print(b)
# a, *b = (80, 90, 100)
#    [90, 100]

# exercise54
# 1. 创建
# --使用元素创建
# dict01 = {"qtx": 100000, "wk": 100000, "bj": 200000}
# # --使用其他容器(该容器内的元素必须能够一分二)
# list01 = [("唐僧", 50000), ["猪八戒", 60000], "沙僧"]
# # {'唐僧': 50000, '猪八戒': 60000, '沙': '僧'}
# dict02 = dict(list01)
# print(dict02)
# # for name,salary in dict01.items():
# #     print(name,salary)
# for items in dict01.items():
#     print(items[0])
#     print(items[1])
#
# for name in dict01:
#     print(name)
# for salary in dict01.values():
#     print(salary)
# # 2. 添加(字典不存在该key)  字典[键] = 值
# if "ss" not in dict01:
#     dict01["ss"] = 700000
#
# # 3. 定位  字典名[键]
# # -- 读取
# print(dict01["wk"])
# # -- 修改
# if "qtx" in dict01:
#     dict01["qtx"] = 500000
#
# # 4. 删除 del 字典名[键]
# del dict01["bj"]

# exercise55
# dict01 = {}
# for number in range(1,11):
#     dict01[number] = number**2
#
# dict01 = {number : number**2 for number in range(1,11) if number % 2 == 0}
# print(dict01)

# exercise56
# set01 = {"悟空", "八戒", "唐三藏"}
# list01 = [10, 20, 30, 20, 30, 40]
# set02 = set(list01)
# print(set02)
# set01.add("白龙马")
# set01.remove("悟空")
# for item in set01:
#     print(item)

# exercise57
# list_city = []
# while True:
#     city = input("请输入疫情地区")
#     if city == " ":
#         break
#     list_city.append(city)
# str_list_city = "_".join(list_city)
# print(str_list_city)
# exercise58
# sentence = "To have a government that is of people by people for people"
# # list_sentence = list(sentence)
# # for i in range(len(list_sentence)-1, -1, -1):
# #     print(list_sentence[i], end = " ")
# list_temp = sentence.split(" ")
# print(list_temp)
# result = " ".join(list_temp[::-1])
# print(result)

# exercise59
# list_number = []
# for number in range(1,51):
#     if number % 3 == 0 or number % 5 == 0:
#         list_number.append(number)
#
# list_number = [number for number in range(1,51) if number % 3 == 0 or number % 5 == 0]
# print(list_number)

# list_number = [num ** 2 for num in range(5,101)]
# print(list_number)

# exercise60
# name = "张无忌"
# name01 = "花无缺"
# names = ["赵敏", "周芷若"]
# # 元组中存储的是变量
# tuple01 = ("张翠山", name, names)
# name = "无忌哥哥"
# name = name01
# # 木有修改元组(修改的是列表)
# tuple01[2][0] = "敏儿"
# # names[0] = "敏儿"
# # tuple01[0] = "山儿"
# print(tuple01)  # ('张翠山', '张无忌', ['敏儿', '周芷若'])

# exercise61
# month = int(input("请输入月份:"))
# tuple_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# print(tuple_days[month - 1])

#exercise62
# dict_epidemic_of_Hong_Kong = {
#     "region": "香港", "now": 6,
#     "current": 53, "total": 1099, "cure": 1042}
#
# dict_epidemic_of_guangzhou = {
#     "region": "广州", "now": 25,
#     "current": 1, "total": 996, "cure": 990}
#
# dict_epidemic_of_neimeng = {
#     "region": "内蒙古", "now": 0,
#     "current": 21, "total": 235, "cure": 213}
#
# dict_epidemic_of_Hong_Kong["死亡"] = 0
# dict_epidemic_of_guangzhou["死亡"] = 1
# dict_epidemic_of_neimeng["死亡"] = 2
#
# del dict_epidemic_of_Hong_Kong["now"]
# dict_epidemic_of_guangzhou["now"] = 0
#
# print(f"{dict_epidemic_of_neimeng['region']}新增{dict_epidemic_of_neimeng['now']}, "
#           f"现有{dict_epidemic_of_neimeng['current']}, 累计{dict_epidemic_of_neimeng['region']},"
#           f" 治愈{dict_epidemic_of_neimeng['cure']}, si亡{dict_epidemic_of_neimeng['死亡']}")

# #exercise63
# list_name = ["张无忌","赵敏","周芷若"]
# room_list = [101,102,103]
# dict_info = { }
# # for i in range(len(list_name)):
# #     dict_info[room_list[i]] = list_name[i]
# # print(dict_info)
#
# dict_info = {room_list[i] : list_name[i] for i in range(len(list_name))}
# print(dict_info)
# # dict_info = { }
# # for i in range(len(list_name)):
# #     dict_info[list_name[i]] = room_list[i]
# # print(dict_info)
#
# result = {v:k for k,v in dict_info.items()}
# print(result)


# list_ticket = []
# while len(list_ticket) < 6:
#     # len(list_ticket) + 1 : 第一次列表长度是0,但是显示应该是1
#     number = int(input("请输入第%d个红球号码：" % (len(list_ticket) + 1)))
#     if number in list_ticket:
#         print("号码已经存在")
#     elif number < 1 or number > 33:
#         print("号码不在范围内")
#     else:
#         list_ticket.append(number)
#
# while len(list_ticket) < 7:
#     number = int(input("请输入蓝球号码："))
#     if number < 1 or number > 16:
#         print("号码不在范围内")
#     else:
#         list_ticket.append(number)
#
# print(list_ticket)

import random

list_ticket = []
# for number in range(6): # 不是预定次数循环,因为可能某一次产生的随机数与前面重复
while len(list_ticket) < 6: # 条件:列表元素不足6个
    number = random.randint(1, 33)
    if number in list_ticket:
        continue
    list_ticket.append(number)

list_ticket.append(random.randint(1, 16))
print(list_ticket)
