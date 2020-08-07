"""将列表中所有元素转换为一个字符串
    列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
    结果:我爱你python666
  注意：列表中包含非字符串数据
    """
list_all = ["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]

list02 = []
for i in range(len(list_all)):
    list02.append(str(list_all[i]))

print("".join(list02))