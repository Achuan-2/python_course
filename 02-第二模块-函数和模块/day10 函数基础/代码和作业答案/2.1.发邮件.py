import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr



def send_email(sender,receiver, password, content):
    # ### 1.邮件内容配置 ###

    # ### 2.发送邮件 ###
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(sender, password)
    server.sendmail(sender, receiver, content)
    server.quit()

def main():

    # 配置
    sender="achuan-2@foxmail.com"
    receiver = "achuan-2@outlook.com"
    password = "klhknkiyfwfqbjdd"

    # 邮件文本
    text = '<a href="https://github.com/WuPeiqi/python_course">WuPeiqi/python_course: 路飞学城Python全新2.0版本课程（Python3.9） (github.com)</a>'
    msg = MIMEText(text, 'html', 'utf-8')
    msg['From'] = formataddr(["Achuan-2", "achuan-2@foxmail.com"])
    msg['Subject'] = "想学python吗"
    content=msg.as_string()

    send_email(sender, receiver, password, content)

if __name__=="__main__":
    main()
