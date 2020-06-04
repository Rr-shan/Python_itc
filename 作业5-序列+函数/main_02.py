
'''
数字出现次数排序

【问题描述】
给定n个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。
【输入形式】
第一行包含一个整数n，表示给定数字的个数; 第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。
【输出形式】
输出有多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序输出。如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。
【样例输入】
12
5 2 3 3 1 3 4 2 5 2 3 5
【样例输出】
3 4
2 3
5 3
1 1
4 1
'''

n = input()
str = input()
# str = '5 2 3 3 1 3 4 2 5 2 3 5'
ls = str.split(' ')


import numpy as np
ls_01 = np.unique(ls)

count_01 = []
for i in ls_01:
    count_01.append(ls.count(i))

dict_01 = dict(zip(ls_01, count_01))
dict_02 = sorted(dict_01.items(), key=lambda d: d[1], reverse=True)

ls_02 = []
for i in range(len(dict_02)):
    ls_02.append(list(dict_02[i]))

for i in range(len(ls_02)):
    for j in range(2):
        print(ls_02[i][j],end=' ')
    print()

# print(ls_01)
# print(count_01)
# print(dict_01)
# print(dict_02)
# print(ls_02)

# 果然这个是没有排序的