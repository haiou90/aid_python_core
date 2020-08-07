#判断
#isspace() 判断是否全都为空白字符
# res = 'this is a test string'.isspace()
# print(res)
# res = '   '.isspace()
# print(res)#True

#isalpha() 判断是否只包含字母
# res = 'abcd'.isalpha()
# print(res)

#isdigit() 判断是否只包含数字字符
# res = '12345'.isdigit()
# print(res)

#isdigit() 判断是否只包含数字字母
# res = '1234abcd'.isalnum()
# print(res)

# str1 = 'this is a test string'
# res = str1.startswith('this')
# print(res)
# res = str1.endswith('ing')
# print(res)

#查找
# str1 = 'this is a test string'
# #       012
# res = str1.find('is')
# print(res)
# res = str1.find('that')
# print(res)
# res = str1.count('at')
# print(res)

# str1 = 'this is a test string'
# res = str1.replace('is','at',1)
# print(str1)
# print(res)
# str1 = '  hello  '
# res = str1.strip()
# str1 = '**hello**'
# res = str1.strip('*')
# res = str1.lstrip('*')
# res = str1.rstrip('*')
# print(res)