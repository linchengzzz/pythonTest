import re


def main():
    username = input('name: ')
    qq = input('qq: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}', username)
    if not m1:
        print('please input username')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('please input qq')
    if m1 and m2:
        print('ok')


if __name__ == '__main__':
    main()
