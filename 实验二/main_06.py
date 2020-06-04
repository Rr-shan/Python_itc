
'''
杨辉三角形

【问题描述】
在屏幕上显示如下杨辉三角形：
                             1
                         1      1
                     1      2      1
                 1       3     3       1
             1       4      6      4       1
         1       5      10     10      5       1
【输入形式】
从键盘输入整数n（n>=0且n<=12）
【输出形式】
在屏幕上输出n+1行杨辉三角形。
【输入样例】
3
【输出样例】
------***1
----***1***1
--***1***2***1
***1***3***3***1
其中－和*都是空格位
即每个数字占四位！
【输出样例说明】
每个数字占四位。这意味着，数字12的输出形式是**12， 这里**代表两个空格。数字330的输出形式是*330。这里*代表一个空格。
要输出占4格的数字num，使用以下语句：
      print("%4d" % num)
%4d是指输出一个整数，其中的4表示占4格。
【评分标准】
结果完全正确得20，每个测试点4分。
'''

def create(l):
    L = [1]
    for x in range(1, len(l)):
        L.append(l[x] + l[x-1])
    # L = [(l[x] + l[x-1]) for x in range(1,len(l))]
    L.append(1)
    return L


def cout(L, W):
    str1 = ""
    for x in L:
        if int(x) < 10:
            str1 += "   " + str(x)
        elif int(x) < 100:
            str1 += '  ' + str(x)
        else:
            str1 += ' ' + str(x)
    print(str1.center(W))

L = [1]
n = int(input())
wid = n*5
for x in range(n + 1):

    for i in range(len(L)):
        print("%4d" % L[i],end='')
    print()
    # cout(L,wid)
    L = create(L)

