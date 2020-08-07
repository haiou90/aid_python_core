"""
-- 定义函数,查找攻击比例atk_rate大于1的所有技能
    -- 定义函数,查找消耗法力cost_sp为零并且持续时间duration大于5的所有技能
    -- 定义函数,查找名称为"九阳神功"的单个技能对象
    -- 定义函数,查找消耗法力最大的单个技能对象
    -- 定义函数,根据持续时间,对技能列表升序排列
    -- 定义函数,判断技能列表中是否存在名称相同的技能对象
              有true没有false(要求:自定义算法实现)
"""

class Skill:
    def __init__(self, name="", atk_rate=0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration


list_skill = [
    Skill("六脉神剑", 0.5, 20, 3),
    Skill("双剑合璧", 1.2, 0, 6),
    Skill("九阳神功", 1.5, 9, 4),
    Skill("玉女心经", 0.8, 0, 8),
    Skill("降龙十八掌", 2, 15, 9),
    Skill("乾坤大挪移", 2, 0, 10),
]
# - 定义函数,查找攻击比例atk_rate大于1的所有技能
def find_skill_gt_1():
    for skill in list_skill:
        if skill.atk_rate > 1:
            yield skill

for skill in find_skill_gt_1():
    print(skill.__dict__)

#     -- 定义函数,查找消耗法力cost_sp为零并且持续时间duration大于5的所有技能
def find_cost_sp_0_duration_gt_5():
    for skill in list_skill:
        if skill.cost_sp == 0 and skill.duration > 5:
            yield skill

for skill in find_cost_sp_0_duration_gt_5():
    print(skill.__dict__)
#     -- 定义函数,查找名称为"九阳神功"的单个技能对象
def find_skill_by_name():
    for skill in list_skill:
        if skill.name == "九阳神功":
            return skill


print(find_skill_by_name().__dict__)
#     -- 定义函数,查找消耗法力最大的单个技能对象
def find_max_skill_by_cost_sp():
    max_value = list_skill[0]
    for i in range(len(list_skill)):
        if max_value.cost_sp < list_skill[i].cost_sp:
            max_value = list_skill[i]
    return max_value

print(find_max_skill_by_cost_sp().__dict__)

#     -- 定义函数,根据持续时间,对技能列表升序排列
def asceding_skill_by_duration():
    for r in range(len(list_skill)-1):
        for c in range(r+1,len(list_skill)):
            if list_skill[r].duration > list_skill[c].duration:
                list_skill[r],list_skill[c] = list_skill[c],list_skill[r]
asceding_skill_by_duration()
for skill in list_skill:
    print(skill.__dict__)

#     -- 定义函数,判断技能列表中是否存在名称相同的技能对象
#               有true没有false(要求:自定义算法实现)

def find_repetion_skill_by_name():
    for r in range(len(list_skill)-1,0,-1):
        for c in range(r-1):
            if list_skill[r].name == list_skill[c].name:
                return True
    else:
        return False

print(find_repetion_skill_by_name())
