
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


import abc

class Pet(object, metaclass=abc.ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname
    