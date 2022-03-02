"""
7. 基于函数实现用户认证，要求：

  - 写函数，读取的用户信息并构造为字典（用户信息存放在`files/user.xlsx`文件中）

     <img src = "assets/image-20201220144654241.png" alt = "image-20201220144654241" style = "zoom:50%;" / >

     ```python
     # 构造的字典格式如下
     user_dict = {
         "用户名": "密码"
         ...
     }
     ```

   - 用户输入用户名和密码，进行校验。（且密码都是密文，所以，需要将用户输入的密码进行加密，然后再与Excel中的密文密码进行比较）

    ```python
     import hashlib

     def encrypt(origin):
         origin_bytes = origin.encode('utf-8')
         md5_object = hashlib.md5()
         md5_object.update(origin_bytes)
         return md5_object.hexdigest()

     p1 = encrypt('admin')
     print(p1)  # "21232f297a57a5a743894a0e4a801fc3"

     p2 = encrypt('123123')
     print(p2)  # "4297f44b13955235245b2497399d7a93"

     p3 = encrypt('123456')
     print(p3)  # "e10adc3949ba59abbe56e057f20f883e"
     ```


扩展：密码都不是明文。

- 注册京东，京东存储：用户名和密码（密文）
- 登录京东：用户名 & 密码。

"""


import hashlib
from openpyxl import load_workbook


def get_user_dict():
    user_dict = {}
    wb = load_workbook("files/user.xlsx")
    sheet = wb.worksheets[0]
    for row in sheet.rows:
        user_dict[row[1].value] = row[2].value
    return user_dict


def encrypt(origin):
    origin_bytes = origin.encode('utf-8')
    md5_object = hashlib.md5()
    md5_object.update(origin_bytes)
    return md5_object.hexdigest()


user = input("请输入用户名：")
pwd = input("请输入密码：")

encrypt_password = encrypt(pwd)

user_dict = get_user_dict()

db_password = user_dict.get(user)

if encrypt_password == db_password:
    print("登录成功")
else:
    print("登录失败")
