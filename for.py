# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)

# sum = 0
# for x in range(1, 101):
#     if x % 2 == 0:
#         sum += x
# print(sum)

# import random
#
# answer = random.randint(1, 100)
# counter = 0
#
# while True:
#     counter += 1
#     number = int(input('input: '))
#     if number < answer:
#         print('da')
#     elif number > answer:
#         print('xiao')
#     else:
#         print('ok')
#         break
# print('一共%d次' % counter);
# if counter > 7:
#     print('智商不足')

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d' % (j, i, i * j), end='\t')
#     print()

# from math import sqrt
#
# num = int(input('num: '))
# end = int(sqrt(num))
#
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d is prime' % num)
# else:
#     print('%d is not prime' % num)

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     (x, y) = (y, x)
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d 和 %d 的最大公约数: %d' % (x, y, factor))
#         print('%d 和 %d 的最小公倍数: %d' % (x, y, x * y // factor))
#         break

# 打印三角形

row = int(input('row = '))

for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
