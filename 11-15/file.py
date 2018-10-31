# def main():
#     f = open('./11-15/1.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()


# if __name__ == '__main__':
#     main()


# def main():
#     f = None
#     try:
#         f = open('./11-15/1.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('no file')
#     except LookupError:
#         print('error encoding')
#     except UnicodeDecodeError:
#         print('unicode error')
#     finally:
#         if f:
#             f.close()


# if __name__ == '__main__':
#     main()


# import time


# def main():
#     with open('./11-15/1.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
    
#     with open('./11-15/1.txt', 'r') as f:
#         for line in f:
#             print(line, end=' ')
#             time.sleep(0.5)
#     print()

#     with open('./11-15/1.txt') as f:
#         lines = f.readlines()
#     print(lines)


# if __name__ == '__main__':
#     main()


import math


def is_prime(n):
    assert n > 0
    for factor in range(2, int(math.sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')