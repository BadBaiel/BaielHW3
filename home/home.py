class Calculator():
    def __init__(self, x, y, ):
        self.x = x
        self.y = y

    def __add__(self):
        print(self.x + self.y)
    def __sub__(self):
        print(self.x - self.y)
    def __mul__(self):
        print(self.x * self.y)
    def __truediv__(self):
        print(self.x / self.y)
x = int(input("Первое значение: "))
y = int(input('Второе значение: '))

calculator = Calculator(x, y)

print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")
oper = int(input('Введите операцию'))
if oper == 1:
    print(calculator.__add__())
elif oper == 2:
    print(calculator.__sub__())
elif oper == 3:
    print(calculator.__mul__())
elif oper == 4:
    print(calculator.__truediv__())
else:
    print('Неправильный ввод')