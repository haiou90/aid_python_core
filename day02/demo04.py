"""
    变量其他写法
    删除变量
    练习：exercise04
"""
# 写法1：变量名 = 数据
data01 = "悟空"
# print(data01)
# 写法2：变量名1, 变量名2 = 数据1, 数据2
data02, data03 = "八戒", "唐僧"
print(data02)  # "八戒"
print(data03)  # "唐僧"
# 写法3：变量名1 = 变量名2 = 数据
data04 = data05 = "沙僧"
print(data05)


data01 = "大圣"
print(data01)
del data02 # 删除变量data02,数据"八戒"引用计数为0所有被销毁
del data04 # 删除变量data04,数据"沙僧"引用计数为1