import math
import fire


class Maths(object):

    def __init__(self, coeff):
        self.coeff = coeff

    def pi(self, n):
        s = 0.0
        for i in range(n):
            s += 1.0/(i+1)/(i+1)
        return self.coeff * math.sqrt(6*s)

    def fact(self, n):
        s = 1
        for i in range(n):
            s *= (i+1)
        return self.coeff * s


if __name__ == '__main__':
    fire.Fire(Maths)


"""
因为Maths的构造器带有参数，所有运行命令行时需要指定构造器参数值
> python maths.py pi 1000 --coeff=2
6.28127611241
> python maths.py pi 1000
ERROR: The function received no value for the required argument: n
Usage: maths.py pi SELF N

For detailed information on this command, run:
  maths.py pi --help
"""