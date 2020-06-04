
'''
集合相似度

【问题描述】
集合相似度是常见的方法，比如：给定两个整数集合，它们的相似度定义为：Nc /Nt×100%。其中Nc是两个集合都有的不相等整数的个数，Nt是两个集合一共有的不相等整数的个数。你的任务就是计算任意一对给定集合的相似度。
【输入形式】
输入第一行给出一个正整数N（≤50），是集合的个数。随后N行，每行对应一个集合。每个集合首先给出一个正整数M（≤10^4），是集合中元素的个数；然后跟M个[0,10 ^ 9]区间内的整数。
【输出形式】
计算第一组与其他每一个集合的相似度，输出其中相似度最高的那个集合。格式为保留小数点后2位的百分比数字。
【样例输入】
3
3 99 87 101
4 87 101 5 87
6 99 101 18 5 135 18
【样例输出】
87 101 5 87
50.00%
【样例说明】
'''

n = int(input())


str = input()
ls_01 = str.split(' ')
del ls_01[0]  # 移除第一个

mark = []

max_ = [] # 如果大的话，就换，不然就不换，也就是最后输出的

# 分别对比
for i in range(n-1):
    str1 = input()
    ls_02 = str1.split(' ')
    del ls_02[0]
    comm_len = len(set(ls_01) & set(ls_02))
    fenmu = len(set(ls_01) ^ set(ls_02)) + comm_len
    m = comm_len/fenmu
    mark.append(m)
    max_.append(tuple(ls_02))
    # print('{:.2%}'.format(mark))
    # print(max)

x = mark.index(max(mark))
for i in range(len(max_[x])):
    print(max_[x][i],end=' ')

print()
print('{:.2%}'.format(max(mark)))

'''
3
3 99 87 101
4 87 101 5 87
6 99 101 18 5 135 18
'''