
# class Person(object):

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print('%s play air' % self._name)
#         else:
#             print('%s play ddd' % self._name)


# def main():
#     person = Person('w', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     # person.name = 'hhah'


# if __name__ == '__main__':
#     main()

# class Person(object):

#     __slots__ = ('_name', '_age', '_gender')

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age >= 16:
#             print('%s is play air' % self._name)
#         else:
#             print('%s is play ddd' % self._name)


# def main():
#     person = Person('ww', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     person._gender = 'mm'
#     # person._is_gay = True


# if __name__ == '__main__':
#     main()


# import math


# class Triangle(object):

#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c

#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b

#     def perimeter(self):
#         return self._a + self._b + self._c

#     def area(self):
#         half = self.perimeter() / 2
#         return math.sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


# def main():
#     a, b, c = 3, 4, 5
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(Triangle.area(t))
#         print(Triangle.perimeter(t))
#         # print(t.perimeter())
#         # print(t.area())
#     else:
#         print('It is not a Triangle !')


# if __name__ == '__main__':
#     main()


# import time
# import os

# class Clock(object):

#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     @classmethod
#     def now(cls):
#         ctime = time.localtime(time.time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


# def main():
#     clock = Clock.now()
#     while True:
#         os.system('clear')
#         print(clock.show())
#         time.sleep(1)
#         clock.run()


# if __name__ == '__main__':
#     main()


# class Person(object):

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         print('%s 正在愉快的玩耍.' % self._name)

#     def watch(self):
#         if self._age >= 18:
#             print('%s kk' % self._name)
#         else:
#             print('%s xx' % self._name)


# class Student(Person):

#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade

#     @property
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade

#     def study(self, course):
#         print('%s的%s正在学习%s.' % (self._grade, self._name, course))


# class Teacher(Person):

#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, title):
#         self._title = title

#     def teach(self, course):
#         print('%s%s正在讲%s' % (self._name, self._title, course))


# def main():
#     stu = Student('w', 15, '3')
#     stu.study('math')
#     stu.watch()
#     t = Teacher('l', 20, 'll')
#     t.teach('py')
#     t.watch()


# if __name__ == '__main__':
#     main()


# import abc

# class Pet(object, metaclass=abc.ABCMeta):

#     def __init__(self, nickname):
#         self._nickname = nickname

#     @abc.abstractmethod
#     def make_voice(self):
#         pass


# class Dog(Pet):

#     def make_voice(self):
#         print('%s: www' % self._nickname)


# class Cat(Pet):

#     def make_voice(self):
#         print('%s: mmm' % self._nickname)


# def main():
#     pets = [Dog('wc'), Cat('kd'), Dog('dh')]
#     for pet in pets:
#         pet.make_voice()


# if __name__ == '__main__':
#     main()

import abc
import random


class Fighter(object, metaclass=abc.ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0
    
    @property
    def alive(self):
        return self._hp > 0

    @abc.abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp
    
    def attack(self, other):
        other.hp -= random.randint(15, 25)
    
    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3//4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= random.randint(10, 15)
            return True
        else:
            return False
    
    def resume(self):
        inc_point = random.randint(1, 10)
        self._mp += inc_point
        return inc_point

    def __str__(self):
        return '~~~ %s ATM ~~~\n' % self._name + 'HP: %d\n' % self._hp + 'MP: %d\n' % self._mp


class Monster(Fighter):

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= random.randint(10, 30)
    
    def __str__(self):
        return '~~~ %s LitterMonster ~~~\n' % self._name + 'HP: %d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = random.randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end=' ')


def main():
    u = Ultraman('zcl', 1000, 120)
    m1 = Monster('dd', 250)
    m2 = Monster('bb', 500)
    m3 = Monster('ww', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('======== 第%02d回合 =======' % fight_round)
        m = select_alive_one(ms)
        skill = random.randint(1, 10)
        if skill <= 6:
            print('%s uis attack %s.' % (u.name, m.name))
            u.attack(m)
            print('%s resume magic %d.' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s use magic attack' % u.name)
            else:
                print('%s use magic attack failed' % u.name)
        else:
            if u.huge_attack(m):
                print('%s use huge attack %s.' % (u.name, m.name))
            else:
                print('%s use attack %s.' % (u.name, m.name))
                print('%s resume magic %d.' % (u.name, u.resume()))
        if m.alive > 0:
            print('%s return attack %s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n======= Fight End! =======\n')
    if u.alive > 0:
        print('%s ultraman is win!' % u.name)
    else:
        print('monsters is win!')


if __name__ == '__main__':
    main()
