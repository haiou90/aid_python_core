
"""
    根据工资计算个人社保缴纳费用
    步骤：在终端中录入缴纳基数,根据公式计算,显示缴纳费用
    公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%
"""

base_pay = float(input("请输入社保缴纳基数:"))

fee_pay = base_pay * ( 8 + 2 +0.2 + 12) / 100 + 3

print("缴纳费用"+ str(fee_pay))