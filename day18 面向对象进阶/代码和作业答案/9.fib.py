class Fibs():
    def __init__(self,n=20) -> None:
        self.n = n
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > self.n:
            raise StopIteration
        return self.a
fibs=Fibs()
for each in fibs:
    print(each)

