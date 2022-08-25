import fire

value = "hello"

if __name__ == '__main__':
    fire.Fire()

"""
> python xyz.py value
hello
# upper是字符串自带
> python xyz.py value upper
HELLO
# 减号用来表示参数的结束
> python xyz.py value upper - lower
hello
> python xyz.py value upper - lower - upper
HELLO
"""