def func():
    print(1)
    print(2)
    print(3)

func()

from mail import send_qqemail

receiver = "achuan-2@outlook.com"
subject = "脚本运行完成"
content = f'{__file__}'
# 运行
send_qqemail(receiver, subject, content)
