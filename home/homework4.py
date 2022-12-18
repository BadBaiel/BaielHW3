class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class B(A):
    def A(self, age):
        self.age = age


class D(A):
    def Min(self):
        return f'{self.name} is cooking tasty food'


class C(B):
    def Add(self):
        return f'{self.age * 2}'


class E(D, C):
    def __str__(self):
        return f'{self.name}, {self.age}'


a = E('Baiel', 12)
a.Min()
a.Add()
print(a)
