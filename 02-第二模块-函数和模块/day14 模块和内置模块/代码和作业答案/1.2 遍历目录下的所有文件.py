
import os

"""
要遍历一个文件夹下的所有文件，例如：遍历文件夹下的所有py文件
"""

data = os.walk(".\commons")
for path, folder_list, file_list in data:
    # path 当前文件夹
    # folder_list 当前文件夹下的子文件夹列表
    # file_list 当前文件夹下的文件列表
    for file_name in file_list:
        file_abs_path = os.path.join(path, file_name)
        ext = file_abs_path.rsplit(".", 1)[1]
        if ext == "py":
            print(file_abs_path)
