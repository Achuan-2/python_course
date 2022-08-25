import fire

class Chain(object):

    def __init__(self):
        self.value = 1

    def incr(self):
        print("incr", self.value)
        self.value += 1
        return self

    def decr(self):
        print("decr", self.value)
        self.value -= 1
        return self

    def get(self):
        return self.value

if __name__ == '__main__':
    fire.Fire(Chain)


"""链式调用
> python chains.py incr incr incr decr decr get
incr 1
incr 2
incr 3
decr 4
decr 3
2
"""