from datetime import datetime, timezone, timedelta

v1 = datetime.now()  # 当前本地时间
print(v1, type(v1))  # 2022-02-25 13:45:46.525438 <class 'datetime.datetime'>


v2 = datetime.utcnow()
print(v2)  # 2022-02-25 05:46:07.988987

tz = timezone(timedelta(hours=7))  # 当前东7区时间
v2 = datetime.now(tz)
print(v2)  # 2022-02-25 12:46:46.227060+07:00

val = v1.strftime("%Y-%m-%d %H:%M:%S")
print(val, type(val))  # 2022-02-25 13:48:30 <class 'str'>

text = "2021-11-11"
v1 = datetime.strptime(text, '%Y-%m-%d')  # %Y 年，%m，月份，%d，天。
print(v1)

text = "2021-11-11" # 00:00:00
v1 = datetime.strptime(text, '%Y-%m-%d')  # %Y 年，%m，月份，%d，天。
print(v1)

# 起床时间
text = "8:00" # 00:00:00
v1 = datetime.strptime(text, '%H:%M')  
print(v1)

# 睡眠时间
text = "23:00" # 00:00:00
v2 = datetime.strptime(text, '%H:%M')  
print(v2)
print(v1<v2) # True
print([v1, v2]) # [datetime.datetime(1900, 1, 1, 1, 0), datetime.datetime(1900, 1, 1, 23, 0)]
print(sorted([v1,v2],reverse=True)) # [datetime.datetime(1900, 1, 1, 23, 0), datetime.datetime(1900, 1, 1, 1, 0)]
print(v2-v1)  # 22:00:00
print(v1-v2)  # -1 day, 9:00:00
# 给睡眠时间减一天
v3 = v2 + timedelta(days=-1) #1899-12-31 23:00:00
print(v1-v3)  #  9:00:00
print(type(v1-v3))  # <class 'datetime.timedelta'>
print((v1-v3).seconds/3600)  # 9
