import re

text = "楼主太牛逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，18715017704搞起来呀"

phone_list = re.findall("1[3|5|8|9]\d{9}", text)
print(phone_list)  # ['15131255789']
