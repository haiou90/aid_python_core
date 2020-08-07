"""
在终端中录入4个同学身高,打印最高的值.
算法：
170 160 180 165
假设第一个就是最大值
使用假设的和第二个进行比较, 发现更大的就替换假设的
使用假设的和第三个进行比较, 发现更大的就替换假设的
使用假设的和第四个进行比较, 发现更大的就替换假设的
最后，假设的就是最大的.
"""
student1 = float(input("请录入同学1的身高:"))
student2 = float(input("请录入同学2的身高:"))
student3 = float(input("请录入同学3的身高:"))
student4 = float(input("请录入同学4的身高:"))
assume = student1

if assume < student2:
    assume = student2
elif assume < student3:
    assume = student3
elif assume < student4:
    assume = student4

print("最高身高为" + str(assume))