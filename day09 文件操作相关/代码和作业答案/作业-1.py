"""
1. 基于csv格式实现 用户的注册 & 登录认证。详细需求如下：

   - 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
   - 用户登录时，逐行读取csv文件中的用户信息并进行校验。
   - 提示：文件路径须使用os模块构造的绝对路径的方式。
"""
from email.mime import base
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_file_path = os.path.join(base_dir,'db.csv')

while True:
    choice = input("是否进行用户注册（Y/N）？")
    choice = choice.upper()
    if choice not in {"Y", "N"}:
        print('输入格式错误，请重新输入。')
        continue
    if choice == "N":
        break
    with open(db_file_path, mode='a', encoding='utf-8') as file_object:
        while True:
            user = input("请输入用户名(Q/q退出）：")
            if user.upper() == 'Q':
                break
            pwd = input("请输入密码：")
            file_object.write("{},{}\n".format(user, pwd))
            file_object.flush()
    break

# 用户登录
print("欢迎使用xx系统，请登录！")
username = input("请输入用户名：")
password = input("请输入密码：")
if not os.path.exists(db_file_path):
    print("用户文件不存在")
else:
    with open(db_file_path, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            user, pwd = line.strip().split(',')
            if username == user and pwd == password:
                print('登录成功')
                break
        else:
            print("用户名或密码错误")
