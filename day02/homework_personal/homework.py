"""
 根据父母身高,预测儿子身高.
    步骤:获取父亲身高
        获取母亲身高
        显示儿子身高
    公式:(父亲身高+母亲身高)*0.54
"""
height_father = float(input("请输入父亲身高:"))
height_mother = float(input("请输入母亲身高:"))

son_height = (height_father + height_mother) * 0.54

print("儿子身高"+ str(son_height))


