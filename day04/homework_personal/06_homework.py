"""
9, 根据下列信息提取变量
   使用占位符拼接字符串·
    湖北确诊67802人,治愈63326人,治愈率0.93
	70秒是1分钟零10秒
"""
# province = "湖北"
# diagnose = 67802
# cured = 63326
# cured_percent = cured / diagnose
# print("%s确诊%d人,治愈%d人,治愈率%.2f"
#       % (province, diagnose, cured, cured_percent))
total_seconds = 70
minute = total_seconds // 60
second = total_seconds % 60

print("%d秒是%d分钟零%d秒" % (total_seconds, minute, second))
