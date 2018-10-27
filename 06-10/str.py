# def main():
#     str1 = 'hello'
#     print(str1)
#     print(len(str1))
#     print(str1.capitalize())
#     print(str1.upper())
#     print(str1.find('lo'))
#     print(str1.find('sh'))
#     # print(str1.index('lo'))
#     # print(str1.index('sh'))
#     print(str1.startswith('he'))
#     print(str1.startswith('He'))
#     print(str1.center(20, '*'))
#     print(str1.rjust(50, ' '))
#     str2 = 'abc123456'
#     print(str2[2])
#     print(str2[2:5])
#     print(str2[2:])
#     print(str2[::2])
#     print(str2[::-1])
#     print(str2.isdigit())
#     print(str2.isalpha())
#     print(str2.isalnum())
#     str3 = '  jackfrued@126.com '
#     print(str3)
#     # 获得字符串修剪左右两侧空格的拷贝
#     print(str3.strip())


# def main():
#     set1 = {1, 2, 3, 3, 3, 2}
#     print(set1)
#     print('Length = ', len(set1))
#     set2 = set(range(1,10))
#     print(set2)
#     set1.add(4)
#     set1.add(5)
#     set2.update([11,12])
#     print(set1)
#     print(set2)
#     set2.discard(5)
#     print(set2)
#     set2.discard(5)
#     print(set2)
#     set2.remove(4)
#     print(set2)
#     # set2.remove(4)
#     # print(set2)
#     # for elem in set2:
#     #     print(elem ** 2, end=' ')
#     # print()
#     set3 = set((1,2,3,3,2,1))
#     # print(set3)
#     # print(set3.pop())
#     # print(set3)
#     print('&: ', set1 & set2)
#     print('-: ', set1 - set2)
#     print('|: ', set1 | set2)
#     print('^: ', set1 ^ set2)
#     print('<=: ', set2 <= set1)
#     print('<=: ', set3 <= set1)
#     print('>=: ', set1 >= set2)
#     print('>=: ', set1 >= set3)


# def main():
#     scores = {'111': 10, '222': 20, '333': 30}
#     print(scores['111'])
#     print(scores['222'])
#     for elem in scores:
#         print('%s\t--->\t%d' % (elem, scores[elem]))
#     scores['111'] = 60
#     scores['222'] = 70
#     scores.update(你好=30, 哈哈=50)
#     print(scores)
#     # print(scores['4444'])
#     print(scores.get('444', 30))
#     print(scores.get('111', 40))
#     print(scores)
#     print(scores.popitem())
#     print(scores.popitem())
#     print(scores.pop('111', 3333))
#     scores.clear()
#     print(scores)


# import os
# import time


# def main():
#     content = '12345.....'
#     while True:
#         os.system('clear')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]


# import random
#
#
# def generate_code(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code
#
#
# print(generate_code())


# if __name__ == '__main__':
#     main()


# def get_suffix(filename, has_dot=False):
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''
#
#
# print(get_suffix('1.text', True))


# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2
# 
#
# print(max2([1, 2, 3, 4, 5]))


# def is_leap_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def which_day(year, month, date):
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date


# print(which_day(2018, 9, 10))


# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()


# if __name__ == '__main__':
#     main()


# from random import randrange, randint, sample


# def display(balls):
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%2d' % ball, end=' ')
#     print()


# def random_select():
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls


# def main():
#     n = int(input('num: '))
#     for _ in range(n):
#         display(random_select())


# if __name__ == '__main__':
#     main()


# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('ji' if person else 'fw', end=' ')
 
# if __name__ == '__main__':
#     main()


import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋，请输入位置：' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = '0'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
        choice = input('again ? (yes|no)')
        begin = choice == 'yes'



if __name__ == '__main__':
    main()