"""
1. 请定义一个函数，用于计算一个字符串中字符`a`出现的次数并通过return返回。

- 参数，字符串。
- 返回值，字符串中 a 出现的次数。

"""


def char_count(text):
    count = 0
    for char in text:
        if char == 'a':
            count += 1
    return count


result = char_count("89alskdjf;auqkaaafasdfiojqln")
