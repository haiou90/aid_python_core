"""
    一家公司有如下岗位：
   经理 ："曹操","刘备","孙权"
   技术 ："曹操","刘备","张飞","关羽"
    1. 使用集合存储以上信息.
    2. 是经理也是技术的都有谁?
    3. 是经理也不是技术的都有谁?
    4. 不是经理是技术的都有谁?
    5. 身兼一职的都有谁?
    6. 公司总共有多少人数?"""

set_manager = {"曹操","刘备","孙权"}
set_technique = {"曹操","刘备","张飞","关羽"}
set_manager_technique = set_manager & set_technique
set_manager_not_technique = set_manager -set_technique
set_technique_not_manager = set_technique -set_manager
set_one = set_manager ^ set_technique

set_total = set_technique | set_manager
print(set_manager)
print(set_technique)
print(set_manager_technique)
print(set_manager_not_technique)
print(set_technique_not_manager)
print(set_one)
print(set_total)
