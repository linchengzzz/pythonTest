# import re


# def main():
#     username = input('name: ')
#     qq = input('qq: ')
#     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}', username)
#     if not m1:
#         print('please input username')
#     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not m2:
#         print('please input qq')
#     if m1 and m2:
#         print('ok')


# if __name__ == '__main__':
#     main()


# import re

# def main():
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，不是15600998765，也是110或119，王大锤的手机号才是15600998765。'
#     my_list = re.findall(pattern, sentence)
#     print(my_list)
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())


# if __name__ == '__main__':
#     main()


import re


def main():
    pome = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。，。]', pome)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == '__main__':
    main()
