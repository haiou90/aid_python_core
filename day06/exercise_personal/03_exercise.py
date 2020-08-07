list01 = [34, 45, 5, 65]
# list_result = []
# for number in list01:
#     if number > 10:
#         list_result.append(number)
# print(list_result)

# list_result = [number for number in list01 if number > 10]
# print(list_result)

# list_result = []
# for number in list01:
#     list_result.append(number % 10)
# print(list_result)


# list_result = []
# for number in range(1, 51):
#     if number % 3 == 0 or number % 5 == 0:
#         list_result.append(number)
# print(list_result)
list_result = [number for number in range(1, 51) if number % 3 == 0 or number % 5 == 0]
print(list_result)

# list_result = []
# for number in range(5, 101):
#     list_result.append(number ** 2)
# print(list_result)
# list_result = [number ** 2 for number in range(5, 101)]
# print(list_result)