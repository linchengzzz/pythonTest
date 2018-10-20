# import fn


# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
#
# def lcm(x, y):
#     return x * y // gcd(x, y)
#
#
# print(gcd(10, 15))
# print(lcm(10, 15))

# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return total == num
#
#
# print(is_palindrome(1221))

def foo():
    global a
    a = 200
    print(a)


if __name__ == '__main__':
    a = 100
    foo()
    print(a)
