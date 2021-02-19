class Cal(int):
    def __add__(self, other):
        return int.__add__(self, other)

    def __sub__(self, other):
        return int.__sub__(self, other)

    def __mul__(self, other):
        return int.__mul__(self, other)

    def __truediv__(self, other):
        return int.__truediv__(self, other)


a = Cal(int(input('输入x\n')))
b = Cal(int(input('输入y\n')))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
