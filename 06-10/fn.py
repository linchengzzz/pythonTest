"""
    C（N, M）= N!//M!//(N-M)!
"""


# n = int(input('n = '))
# m = int(input('m = '))
#
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fnm = 1
# for num in range(1, n - m + 1):
#     fnm *= num
#
# print(fn // fm // fnm)

# def factorial(num):
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
#
#
# n = int(input('n = '))
# m = int(input('m = '))
#
# print(factorial(n) // factorial(m) // factorial(n - m))

# import random
#
#
# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += random.randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     return a + b + c
#
#
# print(roll_dice())
# print(roll_dice(3))
# print(add())
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(c=50, a=10, b=200))

# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total
#
#
# print(add())
# print(add(1))
# print(add(1, 2))
#
# def foo():
#     pass
#
#
# def bar():
#     pass
#
#
# if __name__ == '__main__':
#     print(1)
#     foo()
#     print(2)
#     bar()

for x in range(1, 10)[::-1]:
    print(x, end=' ')
