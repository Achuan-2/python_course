from datetime import datetime

while True:
    text = input("请输入内容：")
    if text.upper() == "Q":
        break

    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M")
    file_name = "{}.txt".format(current_datetime)

    with open(file_name, mode='a', encoding='utf-8') as file_object:
        file_object.write(text+"\n")
        file_object.flush()
