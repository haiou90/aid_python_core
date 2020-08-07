sum_item = 0
for item in range(10, 61):
    if item % 10 == 3 or item % 10 == 5 or item % 10 == 8:
        continue
    else:
        sum_item += item
print(sum_item)

sum_item = 0
for item in range(10, 61):
    if item % 10 == 3 or item % 10 == 5 or item % 10 == 8:
        continue
    sum_item += item
print(sum_item)