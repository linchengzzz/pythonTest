# def main():
#     list1 = [1, 3, 5, 7, 100]
#     print(list1)
#     list2 = ['hello'] * 5
#     print(list2)
#     print(len(list1))
#     print(list1[0])
#     print(list1[4])
#     # print(list1[5])
#     print(list1[-1])
#     print(list1[-3])
#     list1[2] = 300
#     print(list1)
#     list1.append(200)
#     print(list1)
#     list1.insert(1, 400)
#     print(list1)
#     list1 += [1000, 2000]
#     print(list1)
#     print(len(list1))
#     list1.remove(300)
#     print(list1)
#     if 1234 in list1:
#         list1.remove(1234)
#     del list1[0]
#     print(list1)
#     list1.clear()
#     print(list1)


# def main():
#     fruits = ['grape', 'apple', 'strawberry', 'wa']
#     fruits += ['hi', 'hello', 'mango']
#     for fruit in fruits:
#         print(fruit.title(), end=' ')
#     print()
#     fruits2 = fruits[1:4]
#     fruits3 = fruits[:]
#     fruits4 = fruits
#     print(fruits3, fruits4)
#     print(fruits2)
#     fruits3[3] = '111'
#     fruits4[3] = '222'
#     print(fruits3, fruits4, fruits)
#     fruits5 = fruits[-3:-1]
#     fruits6 = fruits[::-1]
#     print(fruits5, fruits6)


# def f(x):
#     return len(x)
#
#
# def main():
#     list1 = ['orange', 'apple', 'zoo', 'inter', 'blueberry']
#     list2 = sorted(list1)
#     print(list1, list2)
#     list3 = sorted(list1, reverse=True)
#     list4 = sorted(list2, key=f)
#     print(list3, list4)
#     list1.sort(reverse=True)
#     print(list1)

# import sys
#
#
# def main():
#     f = [x for x in range(1, 10)]
#     print(f)
#     f = [x + y for x in 'ABCDE' for y in '1234567']
#     print(f)
#     # f = [x ** 2 for x in range(1, 1000)]
#     # print(f)
#     # print(len(f))
#     # print(sys.getsizeof(f))
#     for val in f:
#         print(val)


# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
#
# def main():
#     # for val in fib(20):
#     #     print(val)
#     f = fib(20)
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))


def main():
    t = ('zcl', 38, True, 'Beijing')
    print(t)
    print(t[0])
    print(t[3])
    for member in t:
        print(member)
    # t[0] = '111'
    t = ('11', 22, True, 'Beijing')
    print(t)
    person = list(t)
    print(person)
    person[0] = '1122'
    person[1] = 24
    print(person)
    fruits = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits)
    print(fruits_tuple)


if __name__ == '__main__':
    main()
