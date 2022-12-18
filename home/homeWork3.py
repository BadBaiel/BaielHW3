class SuperHero:
    people = 'people'

    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def realname(self):
         return f'{self.name}'
    def hpx2(self):
        return f'{self.health_points*2}'
    def __str__(self):
        return  f'{self.nickname, self.superpower, self.health_points}'
    def __int__(self):
        return len(self.catchphrase)
Hero=SuperHero('Ben', 'Batman','деньги',200,'все хотят от меня шоу')
Hero.realname()
Hero.hpx2()

print(Hero.realname())
print(Hero.hpx2())

class Earth(SuperHero):
    sign = True
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage=False,fly=False):
        super().__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
    def hpx2(self):
        return f'{self.health_points ** 2}'
    def fly_h(self):
        self.fly=True

    def phrase(self):
        print('fly in the True_phrase')


Earth_h = Earth('Bob', 'Stebel', 'laser', 100, 'babushka boi')
Earth_h.hpx2()
Earth_h.phrase()
print(Earth_h.hpx2())


class Air(SuperHero):
    cape = True
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage=False,fly=False):
        SuperHero.__init__(self,name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
    def hpx2(self):
        return  f'{self.health_points **2}'
    def fly_h(self):
        self.fly=True

    def phrase(self):
         print('fly in the True_phrase')

Air_h = Air('carl','invisy', 'invisible', 30, 'where am i')
Air_h.hpx2()
Air_h.phrase()
print(Air_h.hpx2())


class Villain(Air):
    people = 'monster'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage=False,fly=False):
        super().__init__(name,nickname,superpower,health_points,catchphrase,damage=False,fly=False)
    def gen_x(selfs):...
    def crit(self):
        print(f'{self **2}')
evil = Villain('Ivan','kuvalda','strength',300,'я бью 2 раза')
Villain.crit(Air_h.damage)


class Bank:
    people = 1
    def __init__(self, name, balanse):
        self.name = name
        self.balanse = balanse
    def __str__(self):
        return f'{self.balanse}\n' \
               f'{self.name}\n'
    def moneyX(self):
        self.moneyX = int(input('Сколько хотите закинуть: '))
        self.new=self.moneyX+self.balanse
        print(self.new)
    def _kill(self):
        a = input('Напишите kill что бы обнулить счёт')
        if a == 'kill':
            self.balanse=self.moneyX - self.moneyX
        elif a != 'kill':
            print(self.new)
        else:
            print('Error')

    def __J(self):
        self.balanse = self.balanse * 10
        return self.balanse

    def __D(self):
        e = 100
        b = input('Хотите перевести деньги?: ')
        if b == 'Да':
            print(self.balanse + e)
        else:
            print(self.balanse)


balanse = Bank('Super', 0)
print(balanse)
balanse.moneyX()
balanse._kill()
balanse._Bank__J()
balanse._Bank__D()
print(balanse._kill())
print(balanse.moneyX)














