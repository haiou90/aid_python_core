def func01(list_target):
    print(list01)

def func02(*args):
    print(args)

def func03(p1,p2,*,p4,**kwargs):
    print(p1)
    print(p2)
    print(p4)
    print(kwargs)

list01 = [1,2,3]
func01(list01)
func02(*[1,2,3])
func03(10,20,p4 = 30,p5 = 40)