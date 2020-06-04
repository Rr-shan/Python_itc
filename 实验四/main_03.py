
'''
找相差为1的数对

【问题描述】
　　给定n个不同的整数，问这些数中有多少对整数，它们的值正好相差1。
【输入形式】
　　输入的第一行包含一个整数n，表示给定整数的个数。
　　第二行包含所给定的n个整数。
【输出形式】
　　输出一个整数，表示值正好相差1的数对的个数。
【样例输入】
　　6
　　10 2 6 3 7 8
【样例输出】
      3
      2 3
      6 7
      7 8
【样例说明】
　　值正好相差1的数对包括(2, 3), (6, 7), (7, 8)。
'''

n = int(input())
m = input().split()
a = []
for i in range(0, n):
    a.append(int(m[i]))

icount = 0
b = []
for i in range(0, n):
    for j in range(i + 1, n):
        if abs(a[i] - a[j]) == 1:
            icount += 1
            b.append(min(a[i], a[j]))
            b.append(max(a[i], a[j]))
            # print(min(a[i], a[j]),max(a[i], a[j]))
print(icount)

print(b)
k = 0
for k in range(int(len(b)/2)):
    print(b[k], b[k+1])
    k += 2





# n = input()
# str = input()
# ls = str.split(' ')
#
# ls = list(map(int, ls)) # 将列表中的数转为整型
# ls.sort() # 从小到大排序
#
# record = []
# sum = 0
#
# for i in range(len(ls) - 1):
#     if ls[i+1] - ls[i] == 1:
#         sum += 1
#         record.append(ls[i])
#         record.append(ls[i+1])
#
# print(sum)
# k = 0
# for i in range(int(len(record)/2)):
#     print(record[k],record[k+1])
#     k += 2

# 10 2 6 3 7 8


# n = int(input())
# m = input().split()
# print(m)
#
# a = []
# for i in range(0, n):
#     a.append(int(m[i]))
# print(a)
#
# icount = 0
# b = []
# for i in range(0, n):
#     for j in range(i, n):
#         if abs(a[i] - a[j]) == 1:
#             icount += 1
#             b.append((min(i, j), max(i, j)))
# print(icount)
#
# print(b)
# print(' '.join(b))
