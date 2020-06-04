
'''
 找因子

【问题描述】
输入一个大于1的整数，返回一个列表，包含所有能够整除该整数的因子（不包含1和它本身），并且从小到大排序。如果这个数是素数，则输出“(整数) is prime”。
【样例输入】
number:6
【样例输出】
[2, 3]
【样例输入】
number:5
【样例输出】
5 is prime
'''

ls = []

num = int(input())
flag = 1
for i in range(2,num):
    if num % i == 0:
        ls.append(i)
        flag = 0

if flag:
    print("number:" + str(num) + " is prime")
else:
    print("number:",end='')
    print(ls)