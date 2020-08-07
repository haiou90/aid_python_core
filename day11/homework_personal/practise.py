def move_to_right(list_map):
    # global list_merge
    for item in list_map:
        item = item[::-1]
        # merge()
        # item = list_merge
list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2],
]
# move_to_right(list_map)
# print(list_map)

list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2],
]

list_new = []
# for item in list_map:
#     new = list(item.reverse())
#     list_new.append(new)
# print(list_new)

for i in range(len(list_map)):
    list_map[i].reverse()
    new = list_map[i]
    list_new.append(new)
print(list_new)