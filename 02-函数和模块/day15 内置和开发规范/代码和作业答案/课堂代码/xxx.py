"""
文件注释
"""

# 导入模块顺序：内置、第三方、自定义
import re
import random

import requests
from openpyxl import load_workbook

# 全局变量大写
DB = "XXX"


# 函数注释
def do_something():
    """ 函数注释 """

    # TODO 待完成时，下一期实现xxx功能
    for i in range(10):
        pass


def run():
    """ 函数注释 """

    # 对功能代码进行注释
    text = input(">>>")
    print(text)


if __name__ == '__main__':
    run()
