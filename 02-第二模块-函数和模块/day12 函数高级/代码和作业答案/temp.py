def func(val):
    def inner(a1, a2):
        return a1 + a2 + val

    return inner


data_list = []

for i in range(10):
    data_list.append(func(i))

v1 = data_list[0](11, 22)
v2 = data_list[2](33, 11)

print(v1)
print(v2)
