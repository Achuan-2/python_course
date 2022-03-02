import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# ### 1.邮件内容配置 ###
text = '<a href="https://github.com/WuPeiqi/python_course">WuPeiqi/python_course: 路飞学城Python全新2.0版本课程（Python3.9） (github.com)</a>'
msg = MIMEText(text, 'html', 'utf-8')
msg['From'] = formataddr(["武沛齐", "yangliangran@126.com"])
msg['Subject'] = "想学python吗"

# ### 2.发送邮件 ###
server = smtplib.SMTP_SSL("smtp.126.com")
server.login("yangliangran@126.com", "LAYEVIAPWQAVVDEP")
server.sendmail("yangliangran@126.com", "270992395@qq.com", msg.as_string())
server.quit()
