def find_number(list_target,num):
    for r in range(len(list_target)):
        for c in range(len(list_target[r])):
            if num == list_target[r][c]:
                print("True")
    print("没有")

list_target = [[1,2,3,4,5],[7,8,9,10,12]]
num = 11
find_number(list_target,num)

def find_number(list_target,num):
    for line in list_target:
        if num in line:
            return True
    return False

