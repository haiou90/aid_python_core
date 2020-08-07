def func01(*args,**kwargs):
    print(args)
    print(kwargs)
func01()
func01(1,2,3,a=1,b=2,c=3)


def func02(p1,p2="",*args,p3=0,**kwargs):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(kwargs)

func02(1,2,3,4,5,p3=3,a=1,b=2)
func02(1)
# func02(1, 2, 3,4,5,7,8,p3=5, a=1, b=2, c=3)