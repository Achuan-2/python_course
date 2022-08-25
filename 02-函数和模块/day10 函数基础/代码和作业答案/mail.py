import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

sender_name = 'Achuan-2'
sender = "achuan-2@foxmail.com"
password = "klhknkiyfwfqbjdd"


def main():
    # 邮件文本
    receiver = "achuan-2@outlook.com"
    subject = "脚本运行完成"
    content = f'{__file__}'
    # 运行
    send_qqemail(receiver, subject, content)


def send_qqemail(receiver, subject, content):
    # ### 1.邮件内容配置 ###
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = formataddr([sender_name, sender])
    msg['Subject'] = subject
    mail = msg.as_string()
    # ### 2.发送邮件 ###
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(sender, password)
    server.sendmail(sender, receiver, mail)
    server.quit()


if __name__ == "__main__":
    main()
