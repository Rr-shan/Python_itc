
'''
凯撒加密

【问题描述】
        凯撒密码是古罗马凯撒大帝用来保护重要军情的加密系统。这套密码系统在现在看来很低级，但是在古罗马时期还是发挥了重要作用的。
        凯撒密码的根本思想是按照字母表排列顺序将明文中每个字母变换成其后第n个字母。这里，n（n=1~25）被称作秘钥。
        请编写程序，针对不同的输入字符串和移动位数，输出经过凯撒加密之后的字符串。
【输入形式】
第一个输入参数是移动的位数n，中间间隔一个空格之后，第二个输入参数是待加密的原文字符串
【输出形式】
加密后的密文字符串。注意，只加密字母，且不改变字母大小写。待加密的字符串可能存在比如"hello world"的形式，若与第一个参数一起以input的方式输入，在调用split()的时候要注意，会将待加密字符串也一并分割了。split()方法有参数指定分割多少项，建议采用，请上网搜索说明文档。
【样例输入】
5 NUDT
【样例输出】
SZIY
【样例说明】
输入参数中第一个参数'5'表示移动位数n=5，然后将第二个输入参数中每个字母都向后移动5位，得到输出字符串。
'''

m = input()
n,mi = m.split(' ',1)
n = int(n)
secret = ''

small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in mi:
    if i == ' ':
        secret += ' '
    else:
        if 'a' <= i <= 'z':
            secret += small[(small.index(i) + n) % 26]
        elif  'A' <= i <= 'Z':
            secret += big[(big.index(i) + n) % 26]
        else:
            pass

print(secret)


# 原来是变成一个闭环，而不是跑出去，那就可以自己设定

# for i in mi:
#     if i == ' ':
#         secret += ' '
#     else:
#         if 'a' <= chr(ord(i) + n) <= 'z' or 'A' <= chr(ord(i) + n) <= 'Z':
#             secret += chr(ord(i) + n)
#         else:
#             secret += i