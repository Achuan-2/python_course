"""
6. 补充代码，实现敏感词替换的功能。

 ```python

  def change_string(origin):
       # 补充代码，将字符串origin中中的敏感词替换为 **，最后将替换好的值返回。
       data_list = ["苍老师", "波多老师", "大桥"]

   text = input("请输入内容：")
   result = change_string(text)
   print(result)
   ```

"""


def change_string(origin):
    # 补充代码，将字符串origin中中的敏感词替换为 **，最后将替换好的值返回。
    data_list = ["苍老师", "波多老师", "大桥"]
    for item in data_list:
        origin = origin.replace(item, "**")
    return origin


text = input("请输入内容：")
result = change_string(text)
print(result)
