# 4. 根据值，对字典进行升序排列。
#     输入：{"张无忌":201,"赵敏":101,"小昭":105,"周芷若":302}
#     输出：[('赵敏', 101), ('小昭', 105), ('张无忌', 201), ('周芷若', 302)]

def order_dict(dict_target):
    list_target = list(dict_target.items())
    print(list_target)
    for r in range(len(list_target)-1):
        for c in range(r,len(list_target)):
            if list_target[r][1] > list_target[c][1]:
                list_target[r],list_target[c] = list_target[c],list_target[r]
    return list_target

print(order_dict({"张无忌":201,"赵敏":101,"小昭":105,"周芷若":302}))