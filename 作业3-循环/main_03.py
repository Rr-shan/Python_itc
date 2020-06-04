
'''
随机密码

【问题描述】
请编写程序，生成随机密码。具体要求如下：‪‪‪‪‪‫‪‪‪‪‪‪‫‪‪‪‪‪‪‪‪‪‪‪‫‪‪‪‪‪‪‪‪
    （1）使用 random 库，采用 10作为随机数种子。‪‪‪‪‪‫‪‪‪‪‪‪‫‪‪‪‪‪‪‪‪‪‪‪‫‪‪‪‪‪‪‪‪
提示：random.seed(10)
    （2）密码允许字符如下：
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"‪‪‪‪‪‪‪‪‪‪‫‪‪‪‪‪‪‪‪
    （3）密码长度固定为 10 个字符。
【样例输入】
无
【样例输出】
e30bA8!Jue
'''

import random

random.seed(10)

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
password = ""
n = int(input())

while len(password) < n:
    x = ""
    x += s[random.randint(0, len(s) - 1)]
    password += x

print(password)


# import random
# random.seed(10)
# n=input()
# s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# p=int(n)
# ls=list(s)
# ls1=[]
# for i in range(p):
#     o=random.choice(ls)
#     # print(o)
#     ls1.append(o)
# print(ls1)
