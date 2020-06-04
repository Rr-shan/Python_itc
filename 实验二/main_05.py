
'''
矩阵-各列求最大值

【问题描述】编写程序实现：用3*5的整型矩阵a接收标准输入的数据，计算数组a的每列元素的最大值，并将第i列最大值存入max相应的第i个元素。
【输入形式】标准输入的每一行表示矩阵a中的一行数据，以空格作为间隔。
【输出形式】标准输出的一行表示max中的元素，用空格作为间隔；若输入数据不合法（如：小数或某一行数据少于5个），则输出"illegal input"。
【样例输入】
            1 2 3 4 5
            6 7 8 9 0
            3 5 7 9 1
【样例输出】6 7 8 9 5
'''

import numpy as np

# 总的列表
ls_sum = []
for i in range(3):
    str = input()
    # 判断是否含小数点以判断是否是整数
    if '.' in str:
        print('illegal input')
        quit()

    ls = str.split(' ')
    # 将字符串转化为int
    ls_tocheck = [int(ls[i]) for i in range(len(ls))]
    # 个数是否等于5
    if len(ls_tocheck) != 5:
        print('illegal input')
        exit()
    ls_sum.extend(ls_tocheck)


lss = []
ls_max = []
for i in range(5):
    for i in range(i,len(ls_sum),5):
        lss.append(ls_sum[i])
    ls_max.append(max(lss))
    lss.clear()

for i in range(len(ls_max)):
    print(ls_max[i],end=' ')



'''
1 2 3 4 5
6 7 8 9 0
3 5 7 9 1
'''
