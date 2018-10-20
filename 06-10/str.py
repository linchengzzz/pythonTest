
def main():
    str1 = 'hello'
    print(str1)
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('lo'))
    print(str1.find('sh'))
    # print(str1.index('lo'))
    # print(str1.index('sh'))
    print(str1.startswith('he'))
    print(str1.startswith('He'))
    print(str1.center(20, '*'))
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    print(str2[2])
    print(str2[2:5])
    print(str2[2:])
    print(str2[::2])
    print(str2[::-1])
    print(str2.isdigit())
    print(str2.isalpha())
    print(str2.isalnum())
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


if __name__ == '__main__':
    main()
