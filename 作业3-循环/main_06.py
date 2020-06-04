
'''
翻译密码

【问题描述】翻译密码。为了保密，常不采用明文，而用密文，即按一定规则将字符转换为另一字符，收报人则按相反的规律转换得到原来的字符。本程序规则为：字母ascii码加5，其他字符不变，对原文进行加密，并显示密文。字母的最后5个加5不是字母了，处理规则为循环成前5个。比如“X”的密文为“C”。
【样例输入】
please input text:I love haha.
【样例输出】
N qtaj mfmf.
【样例说明】ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符
【评分标准】
'''

# 内置函数 ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符
# I love haha.
exactpwd = input('please input text:')
secretpwd = ''

for i in exactpwd:

    if i>='a' and i<='z':
        if i>='v':
            secretpwd += chr(ord(i)-21)
        else:
         secretpwd += chr(ord(i) + 5)
    elif i>='A' and i<='Z':
        if i>='V':
            secretpwd += chr(ord(i)-21)
        else:
            secretpwd += chr(ord(i)+5)
    else:
        secretpwd += i

print(secretpwd)