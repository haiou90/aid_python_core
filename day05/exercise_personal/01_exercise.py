"""
字符串： content = "我是京师监狱狱长金海。"
打印第一个字符、打印最后一个字符、打印中间字符   索引[i] 从0开始，最大值为总数减1
打印字前三个符、打印后三个字符         切片[:3] [3:]
命题：金海在字符串content中        成员运算符 in
命题：京师监狱不在字符串content中   成员运算符 not in
通过切片打印“京师监狱狱长”[2:8:1] 包含开始值，不包含结束值
通过切片打印“长狱狱监师京”[7:1:-1]
通过切片打印“我师狱海”[::3]间隔为3
倒序打印字符[::-1]
"""
content = "我是京师监狱狱长金海。"
print(content[0])
print(content[-1])
print(content[len(content) // 2])   #地板除取整
print(content[:3])
print(content[-3:])

print("金海" in content)
print("京师监狱" not in content)

print(content[2:8])
print(content[7:1:-1])
print(content[::3])

print(content[::-1])
