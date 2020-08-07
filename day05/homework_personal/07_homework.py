"""

9. 在终端中录入5个疫情省份的确诊人数
   最后打印最大值、最小值、平均值.
   （使用内置函数实现）

"""
list_region = ["香港", "内蒙古", "四川", "台湾", "北京"]
list_diagnose = []
for i in range(len(list_region)):
    amount = int(input("请输入%s的确诊人数" % list_region[i]))
    list_diagnose.append(amount)

print(max(list_diagnose))
print(min(list_diagnose))
print(sum(list_diagnose) / len(list_diagnose))
