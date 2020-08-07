list_result = []
while True:
    number = input("请输入:")
    if number == " ":
        break
    list_result.append(number)
str_result = "-".join(list_result)
print(str_result)