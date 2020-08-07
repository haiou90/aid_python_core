"""
练习:使用装饰器，为旧功能增加新功能(验证权限).
    # 验证权限
"""
"""
def delete():
print("删除成功")

insert()
delete()
"""

def verif_permission(func):  # 得到旧功能
    def wrapper(*args, **kwargs):  # 新功能 + 旧功能
        # 新功能：打印传入的函数名称
        print("验证权限")
        # 旧功能：执行传入的函数
        return func(*args, **kwargs)

    return wrapper


@verif_permission # 调用外部函数  绑定下面函数
def insert(data):
    print("插入成功",data)
    return "yes"

result = insert("10条数据")
print(result)
@verif_permission # 调用外部函数  绑定下面函数
def delete():
    print("插入成功")

delete()


