class Cal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)

    def subtract(self):
        print(self.x - self.y)

    def multiply(self):
        print(self.x * self.y)

    def divide(self):
        print(self.x / self.y)


cal = Cal(int(input('输入x\n')), int(input('输入y\n')))
cal.add()
cal.subtract()
cal.multiply()
cal.divide()
