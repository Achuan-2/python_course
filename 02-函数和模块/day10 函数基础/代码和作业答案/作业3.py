from pydoc import doc


"""
3. 写函数，接收两个数字参数，返回比较大的那个数字（等于时返回两个中的任意一个都可以）。
"""
def get_bigger(num1, num2):
    if num1 > num2:
        return num1
    return num2


result = get_bigger(11, 22)


