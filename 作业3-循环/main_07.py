
'''
Python 判断可逆素数

【问题描述】若将某一素数的各位数字的顺序颠倒后得到的数仍是素数，则此素数称为可逆素数
【输入形式】用户在第一行输入一个整数。
【输出形式】程序输出yes或是no,yes表示此数是可逆素数，no表示不是。用户输入的数必须为正整数。注意：yes或是no全是小写输出。
【样例输入】23
【样例输出】no
【样例说明】用户输入23，23各位数字颠倒之后得到32，23是素数，但32不是素数，所以23不是可逆素数。
【评分标准】
'''

prime = eval(input())
rev = int(str(prime)[::-1])

def isPrime(num):
    i = 2
    while i<num:
        if  num%i == 0:
            return 0
        i += 1
    return 1

if isPrime(prime) and isPrime(rev):
    print('yes')
else:
    print('no')