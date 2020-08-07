list01 = [54,43,23,67,28,69,90]
def get_number(list_target):
    list_result = []
    for number in list_target:
        list_result.append(number % 10)
    return list_result
result = get_number(list01)
print(result)


def get_number(list_target):
    for number in list_target:
        yield number % 10

for num in get_number(list01):
    print(num)