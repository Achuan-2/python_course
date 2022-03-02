"""
4. 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历，然后将这四个值通过"*"拼接起来并追加到一个student_msg.txt文件中。
"""


def write_file(name, gender, age, degree):
    data_list = [name, gender, age, degree]
    data = "*".join(data_list)
    with open('student_msg.txt', mode='a', encoding='utf-8') as file_object:
        file_object.write(data)


write_file("武沛齐", "男", "18", "博士")
