import time

print(time.time())
print(time.localtime())
tuple_time = time.localtime(1592374665.8086662)
print(tuple_time)

print(time.strftime("%Y/%m/%d %H:%M:%S ", tuple_time))
print(time.strptime("2020/06/17", "%Y/%m/%d"))
list_week = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
def calculate_weekday(year,month,day):
    # tuple_time = time.strptime(str(year)+"/"+str(month)+"/"+str(day), "%Y/%m/%d")
    tuple_time = time.strptime(f'{str(year)}/{str(month)}/{str(day)}', "%Y/%m/%d")
    weekday = tuple_time[6]
    # for day in list_week:
    return list_week[weekday]

print(calculate_weekday(2020, 6, 17))
