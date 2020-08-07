confirmed_patient = int(input('请输入确诊人数:'))
cured_patient = int(input('请输入治愈人数:'))

cured_percent = cured_patient / confirmed_patient *100

print("治愈比例为:"+str(cured_percent) +"%")
