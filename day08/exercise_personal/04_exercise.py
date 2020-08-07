# definite_num = int(input("请输入确诊人数："))
# cure_num = int(input("请输入治愈人数："))
# print("治愈比例为：" + str(cure_num / definite_num * 100) + "%")

def cured_percent(definite_num,cure_num):
    result = cure_num / definite_num * 100
    return result
result = cured_percent(100,80)
print(result)