# 01-05 练习项目

# 寻找 100 - 999 之间的水仙花数

for x in range(100, 1000):
    l = x // 10 // 10 % 10
    m = x // 10 % 10
    n = x % 10
    if l ** 3 + m ** 3 + n ** 3 == x:
        print(x)
