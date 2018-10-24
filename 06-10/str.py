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


def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


print(get_suffix('1.text', True))
