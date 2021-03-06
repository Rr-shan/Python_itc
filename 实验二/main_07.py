
'''
解密码

有一行电文，已按下面规律译成密码：
     A--Z   a--z
     B--Y   b--y
     C--X   c--x
     ......
即第1个字母变成第26个字母，第i个字母变成第（26-i+1）个字母; 非字母字符不变。编写程序把密码译回原文，并输出密码和原文。
【输入形式】
输入一串密码（长度为10，可包含数字、字母）
【输出形式】
首先输出密码，然后换行后输出原文
【样例输入】
4sdf&13TBD
【样例输出】
4sdf&13TBD
4hwu&13GYW
【样例说明】
【评分标准】
'''

small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# 第一种反转方式
smallconvert = small[::-1]
big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# 第二种反转方式
bigconvert = list(reversed(big))

str = input()
print(str)
for i in range(len(str)):
    if str[i].isalpha():
        if  str[i].islower():
            print(smallconvert[small.index(str[i])],end='')
        else:
            print(bigconvert[big.index(str[i])],end='')
    else:
        print(str[i],end='')
