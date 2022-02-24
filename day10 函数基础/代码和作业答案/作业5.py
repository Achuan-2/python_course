"""
5. 补充代码，实现如下功能：

- 【位置1】读取文件中的每一行数据，将包含特定关键词的数据筛选出来，并以列表的形式返回。
- 【位置1】文件不存在，则返回None
- 【位置2】文件不存在，输出 "文件不存在"，否则循环输出匹配成功的每一行数据。

```python


def select_content(file_path, key):
    # 补充代码【位置1】

   result = select_content("files/xxx.txt", "股票")
   # 补充代码【位置2】
   ```

"""

import os


def select_content(file_path, key):
    # 补充代码【位置1】
    if not os.path.exists(file_path):
        return
    data_list = []
    with open(file_path, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            if key in line:
                data_list.append(line)
    return data_list


result = select_content("files/xxx.txt", "股票")
if result == None:
    print("文件不存在")
else:
    print(result)
