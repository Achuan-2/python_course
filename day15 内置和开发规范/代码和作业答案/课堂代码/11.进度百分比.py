import time

print("开始下载")
for i in range(1, 101):
    data = "\r{}%".format(i) # \r 输出时会回到这一行的开头
    print(data, end="")
    time.sleep(0.02)

print("\n下载完成")
