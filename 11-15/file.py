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


import time


def main():
    with open('./11-15/1.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    
    with open('./11-15/1.txt', 'r') as f:
        for line in f:
            print(line, end=' ')
            time.sleep(0.5)
    print()

    with open('./11-15/1.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
