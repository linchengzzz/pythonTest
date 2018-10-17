
# f = float(input('请输入: '))
# c = (f - 32) / 1.8
# print('%.1f h = %.1f s'%(f,c))

# import math

# radius = float(input('r: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('l: %.2f' % perimeter)
# print('s: %.2f' % area)

year = int(input('year: '))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)