
'''
读者第几次出现

【问题描述】
　　涛涛最近要负责图书馆的管理工作，需要记录下每天读者的到访情况。每位读者有一个编号，每条记录用读者的编号来表示。给出读者的来访记录，请问每一条记录中的读者是第几次出现。
【输入形式】
　　输入的第一行包含一个整数n，表示涛涛的记录条数。
　　第二行包含n个整数，依次表示涛涛的记录中每位读者的编号。
【输出形式】
　　输出一行，包含n个整数，由空格分隔，依次表示每条记录中的读者编号是第几次出现。
【样例输入】
　　5
　　1 2 1 1 3
【样例输出】
　　1 1 2 3 1
'''

n = input()
str = input()
ls = str.split(' ')

mark = [] # 标记是否访问过
times = [] # 记录来的次数
for i in range(len(ls)):
    if not mark.count(ls[i]):
        times.append(1) # 第一次为1
        mark.append(ls[i]) # 进入+1
    else:
        times.append(mark.count(ls[i])+1) # 已经有的次数再加1
        mark.append(ls[i]) # 进入+1

for i in range(len(times)):
    print(times[i],end=' ')