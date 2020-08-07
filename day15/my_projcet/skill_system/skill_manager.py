# from skill_system.skill_deployer import SkillDeployer #方法一

import skill_system #方法二

class SKillManager:
    def func01(self):
        print("func01执行喽")

# 方法一
# deployer = SkillDeployer()
# deployer.func02()


# 方法二
# 必须在__init__.py中配置
# import skill_system.skill_deployer

# deployer = skill_system.skill_deployer.SkillDeployer()
# deployer.func02()