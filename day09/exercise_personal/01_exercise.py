def calculat_seconds(hour=0, minute=0, second=0):
    seconds = hour * 3600 + minute * 60 + second
    return seconds

result = calculat_seconds(1,20,5)
print(result)
result = calculat_seconds(minute=5,second=5)
print(result)
result = calculat_seconds(2,second=5)
print(result)

result = calculat_seconds(minute=6)
print(result)