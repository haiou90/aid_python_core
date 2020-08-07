def find_no_repetition(chars):
    for r in range(len(chars)):
        if chars[r] not in chars[r + 1:len(chars)] and chars[r] not in chars[:r - 1]:
            return chars[r]

result = find_no_repetition("ABCACDBEFD")
print(result)


def get_repeating_info(target):
    dict_repeat_info = {}
    for char in target:
        # dict_repeat_info[char] = target.count(char)
        if char not in dict_repeat_info:
            dict_repeat_info[char] = 1
        else:
            dict_repeat_info[char] += 1
    return dict_repeat_info


def first_no_repating(target):
    dict_info = get_repeating_info(target)
    for k, v in dict_info.items():
        if v == 1:
            return k


print(first_no_repating('ABCACDBEFD'))
