# 4. 定义函数，返回字符串中第一个不重复的字符。
# 输入：ABCACDBEFD
# 输出：E

#统计字符串中 每一个字符出现的次数 以字典的形式返回
# {'A':2,'B':2...}
def get_repeating_info(target):
    dict_repeat_info = {}
    # 遍历字符串 取出每一个字符 获取数据(出现的次数) 保存到字典
    for char in target:
        # dict_repeat_info[char] = target.count(char)
        if char not in dict_repeat_info:
            dict_repeat_info[char] = 1
        else:
            dict_repeat_info[char] += 1
    print(dict_repeat_info)
    return dict_repeat_info

def firt_not_repeating_char(target):
    dict_info = get_repeating_info(target)
    for k,v in dict_info.items():
        if v == 1:
            return k

print(firt_not_repeating_char('ABCACDBEFDG'))