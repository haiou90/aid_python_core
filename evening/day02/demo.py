# print('abc' > 'ba')
# print([3,12] > [5,3])
# print((1,2) > (2,1))

#短路
# and 一假俱假
# 当前面的条件返回False时  后面的代码就不再执行
# 将简单的容易得到结果的条件写在前面能提升效率
# print(0 and int('abc'))

# a = 'this is a test string'
# b = 'this is a test string'
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# a = 10
# b = 20
# print(a if a > b else b)

list01 = [1,2,3,4,5]
#         0 1 2 3 4
# print(list01[1:])
# print(list01[:])#浅拷贝
# from copy import deepcopy
# print(list01[::-1])
# list01[:] = []
# print(list01)

name = 'QTX'
age = 18
print('姓名：%s,年龄：%s' % (name,age))
# 19:58~20:10
print('姓名：{},年龄：{}'.format(name,age))
print('姓名：{1},年龄：{0}'.format(name,age))
# 让name在10个字符中 ^居中 <靠左 >靠右
# print('姓名：{:>10},年龄：{}'.format(name,age))

qtx = {'name':'qtx','age':18}
# print(qtx['address'])
# get获取字典指定键的值如果键不存在 返回默认值
# get(key,default)
# print(qtx.get('address',-1))

def mymax(a,b):
    # print(a if a > b else b)
    # return None 默认的返回值
    # 结果如果后续还要使用 一定要写return返回
    return a if a > b else b

def fun(a,b):
    print('a和b比较的结果是：',mymax(a,b))
fun(10,20)

