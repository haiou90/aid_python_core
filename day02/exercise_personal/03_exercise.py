price = float(input('请输入单价:'))
amount = float(input('请输入数量:'))
money_pay = float(input('请输入金额:'))

money_return = money_pay -price * amount

print('应找回:%.1f元' % money_return)
