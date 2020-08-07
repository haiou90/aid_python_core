# def fun(name):
#     # print('hello world')
#     print('hello',name)
#
#
# # fun()
# fun('QTX')

# def myadd(a, b=10):
#     return a + b
#
# myadd(5,5)
# myadd(b=5,a=10)

# def fun2(a,b,c,d,e):
#     print(a,b,c,d,e)

# dict01 = {'a':10,'b':20,'c':30,'d':40,'e':50}
# #**拆解字典,以关键字方式传值 a=10 b=20 ...
# fun2(**dict01)


# tuple01 = (10,20,30,40,50)
# fun2(*tuple01)

# str01 = 'abced'
# fun2(*str01)

# list01 = [10,20,30,40,50]
#*在实参中 表示拆解序列 将拆解到的序列中的元素按位置传递给函数
# fun2(*list01)

# fun2(10,20,30,e=50,d=40)
# SyntaxError: positional argument follows keyword argument
# 语法错误:位置参数跟在关键字参数后面(要先写位置参数 后写关键字参数)
# fun2(a=10,b=20,30,40,50)
# TypeError: fun2() got multiple values for argument 'a'
# 类型错误:fun2()中的参数a有多个值
# fun2(10,20,30,a=40,b=50)

# def myprint(*data,**kwdata):
#     # *data 以元组的形式 接受任意数量的实参
#     print(data)
#     # print(**kwdata)#报错 将字典拆解开以后传递给print
#     print(kwdata)
#     for i in kwdata:
#         print(i,kwdata[i])
#
# # myprint(10,20,30)
# myprint(a=10,b=20)

# 20:05~20:15
def fun3(a,b,c=30,*args,name='',age=0,**kwargs):
    print(a,b,c)
    print(name,age)
    print(args)
    print(kwargs)

# fun3(10,20,30)
fun3(10,20,30,'maira',18,name='QTX',age=18)









