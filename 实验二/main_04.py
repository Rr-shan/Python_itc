
'''
统计正负数个数

【问题描述】从键盘输入非0整数，以输入0为输入结束标志，求平均值，统计正数负数个数
【输入形式】
      每个整数一行。最后一行是0，表示输入结束。
【输出形式】
     输出三行。
     第一行是平均值。第二行是正数个数。第三行是负数个数。
【样例输入】
                        1
                        1
                        1
                        0
【样例输出】
                        1
                        3
                        0
'''

ls = []

# 输入的方式出现了问题
while 1:
    n = input()
    if n != '0':
        ls.append(n) # += 列表操作会出现问题
    else:
        break


# 负数居然会被划分到开来
l = len(ls)
sum = 0
count_1 = 0
for i in range(l):
    if int(ls[i]) > 0:
        count_1 += 1
    sum += int(ls[i])

count_2 = l - count_1

print(sum / l)
print(count_1)
print(count_2)

# 1、-1、0

def countt():
    ls_01 = []
    while 1:
        n = input()
        if n != '0':
            ls_01.append(n)
        else:
            break
    l = len(ls_01)
    sum = 0
    count = 0
    for i in range(l):
        if int(ls_01[i]) > 0:
            count += 1
        sum += int(ls_01[i])

    count_1 = l - count
    print(sum / l)
    print(count)
    print(count_1)

countt()