"""
    函数内存分布
    1. 传入可变对象
    2. 修改可变对象
    3. 函数外可以得到结果(不用return)
    练习:exercise10
"""

# 将函数的代码存储到代码区中
def func01(p1, p2):
    p1[0] = 100  #改变的是栈帧外的列表元素
    p2 = 200     #改变的是栈帧中的变量P2

list01 = [10]
list02 = [20]
# 调用函数在内存中开辟一块空间(栈帧),
# 用于存储在函数中创建的变量
func01(list01, list02)
# 函数执行后栈帧释放
print(list01[0])  # 100
print(list02[0])  # ?

def fun(p1,p2,p3):
    p1[0] = 100
    p2 = 200
    p3 = "ab"

list01=[10]
list02=[20]
str03 = "abc"
fun(list01,list02,str03)
print(list01,list02,str03)