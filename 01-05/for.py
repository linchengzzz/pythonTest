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
#
# row = int(input('row = '))
#
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

# fibonacci

# a = 0
# b = 1
# for _ in range(20):
#     (a, b) = (b, a + b)
#     print(a, end=' ')

# 100 100
# x = 5
# y = 3

# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if x * 5 + y * 3 + z / 3 == 100:
#             print(x, y, z)

# 赌博游戏

# import random
#
# money = 1000
#
# while money > 0:
#     print('你得资产为：', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注：'))
#         if debt > 0 and debt <= money:
#             break
#     first = random.randint(1, 6) + random.randint(1, 6)
#     print('玩家摇出了%d点。' % first)
#     if first == 7 or first == 11:
#         print('玩家胜！')
#         money += debt
#     elif first == 2 or first ==3 or first == 12:
#         print('庄家胜！')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         current = random.randint(1, 6) + random.randint(1, 6)
#         print('玩家摇出了%d点。' % current)
#         if current == 7:
#             print('庄家胜！')
#             money -= debt
#             needs_go_on = False
#         elif current == first:
#             print('玩家胜！')
#             money += debt
#             needs_go_on = False
#
# print('没钱游戏结束！')

# num1 = int(input('num1 = '))
# temp = num1
# num2 = 0
# while temp > 0:
#     num2 *= 10
#     num2 += temp % 10
#     temp //= 10
# if num1 == num2:
#     print('ok')
# else:
#     print('false')

import time
import math

start = time.clock()
for num in range(1, 10000):
    _sum = 0
    for fac in range(1, int(math.sqrt(num)) + 1):
        if num % fac == 0:
            _sum += fac
            if 1 < fac != num / fac:
                _sum += num / fac
    if _sum == num:
        print(num)

end = time.clock()
print('time', (end - start))
