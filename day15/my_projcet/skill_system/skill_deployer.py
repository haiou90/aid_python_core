# from common.list_helper import ListHelper #方法一

from common import  *    #方法二 使用第三方模块时
# 在__init__.py中配置
# __all__ = ["list_helper"]

# 导入模块是否成功的唯一标准：
# 导入路径 + sys.path = 实际路径
#程序执行的根目录skill_system与认为的根目录my_projcet不一致时,会出错
# 1.导入路径common
# 2.sys.path
import sys
# sys.path.append("/home/tarena/month01/code/day15/my_projcet")
print(sys.path)
# 3.实际路径
#能够导入模块的实际目录/home/tarena/month01/code/day15/my_projcet/common
#程序执行的根目录 /home/tarena/month01/code/day15/my_projcet/skill_system
# 导入路径是在根目录内开始写起来的即my_projcet/skill_system,
# 但是common.list.py不在skill_system里,而是在my_projcet/common里
# mark as SourceRoot,相当于强制设置了根目录

class SkillDeployer:
    def func02(self):
        print("func02执行了")

# ListHelper.func03() #方法一
list_helper.ListHelper.func03()  #方法二

