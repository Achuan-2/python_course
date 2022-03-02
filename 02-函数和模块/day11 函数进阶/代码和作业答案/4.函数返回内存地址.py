def func():
    data = 123123
    print(id(data))
    return data


v1 = func()
print(v1, id(v1))  
"""
2067864324368
123123 2067864324368
"""

v2 = func()
print(v2, id(v1))  
"""
2067864324368
123123 2067864324368
"""
