def foo():
    yield 2
    yield 2
    yield 2


def func():
    yield 1
    yield 1
    yield 1
    yield from foo()
    yield 1
    yield 1


for item in func():
    print(item)
