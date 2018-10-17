# username = input('username: ')
# password = input('password: ')
# if username == 'admin' and password == '123456':
#     print('ok')
# else:
#     print('no')

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x >= -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('l: %.2f' % (a + b + c))
    p = (a + b + c) / 2
    ares = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('s: %.2f' % ares)
else:
    print('error')
