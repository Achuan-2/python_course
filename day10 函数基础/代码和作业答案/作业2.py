"""
2. 写函数，判断用户传入的一个值（字符串或列表或元组任意）长度是否大于5，并返回真假。
"""


def judge_length(data):
    if len(data) > 5:
        return True
    return False


result = judge_length("武沛齐武沛齐")
print(result)
