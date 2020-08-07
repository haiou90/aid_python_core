"""
列表推导式练习：
  计算1970年到2050年之间所有闰年
"""
year_run = []
for year in range (1970, 2051):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        year_run.append(year)
print(year_run)