# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print('%s333%s' % (self.name, course_name))
#
#     def watch_av(self):
#         if self.age < 18:
#             print('%s 111 .' % self.name)
#         else:
#             print('%s 222 .' % self.name)
#
#
# def main():
#     stu1 = Student('zcl', 20)
#     stu1.study('py')
#     stu1.watch_av()
#     stu2 = Student('mz', 11)
#     stu2.study('sx')
#     stu2.watch_av()
#
#
# if __name__ == '__main__':
#     main()


# class Test:
#     def __init__(self, foo):
#         self.__foo = foo

#     def bar(self):
#         print(self.__foo)
#         print('__bar')


# def main():
#     test = Test('hello')
#     test.bar()
#     print(test.__foo)


# if __name__ == '__main__':
#     main()


# import time

# class Clock(object):

#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second

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
                
#     def __str__(self):
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock)
#         time.sleep(1)
#         clock.run()


# if __name__ == '__main__':
#     main()


import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()