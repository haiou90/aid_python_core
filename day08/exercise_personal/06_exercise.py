"""
    输入课程阶段数,显示课程名称
    1 显示 Python语言核心编程
    2 显示 Python高级软件技术
    3 显示 Web 全栈
    4 显示 网络爬虫
    5 显示 数据分析、人工智能
"""
# number = input("请输入课程阶段数：")
# if number == "1":
#     print("Python语言核心编程")
# elif number == "2":
#     print("Python高级软件技术")
# elif number == "3":
#     print("Web全栈")
# elif number == "4":
#     print("网络爬虫")
# elif number == "5":
#     print("数据分析、人工智能")

def find_course(count):
    list_course = ["1 显示 Python语言核心编程",
                   "2 显示 Python高级软件技术",
                   "3 显示 Web 全栈",
                   "4 显示 网络爬虫",
                   "5 显示 数据分析、人工智能"]
    if 1 <= count <= len(list_course):
        return list_course[count-1]
    return "课程不存在"
result = find_course(1)
print(result)


def find_course(count):
    """
    查找课程名称
    :param count:课程阶段
    :return: 返回课程名称
    """
    dict_course = {1: "显示 Python语言核心编程",
                   2: "显示 Python高级软件技术",
                   3: "显示 Web 全栈",
                   4: "显示 网络爬虫",
                   5: "显示 数据分析、人工智能"}
    return dict_course[count]

result = find_course(1)
print(result)