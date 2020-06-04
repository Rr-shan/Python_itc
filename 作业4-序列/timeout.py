
'''
测试时间！！
'''

n = int(input()) # TODO：这个没有起到控制数量的作用
ls = list(map(int, input().strip().split()))
x = list(set(ls)) # 去重复
list.sort(x) # 排序

num = []
for i in x:
    num.append(ls.count(i))

m = max(num) # 求最大数

for i in range(len(num)):
    if num[i] == m:
        print(x[i],end=' ')
        print(m)



n = int(input())
ls = list(map(int, input().strip().split()))

x = list(set(ls))

num = []
for i in x:
    num.append(ls.count(i))
m = max(num)
for i in range(len(num)):
    if num[i] == m:
        print(x[i],end=' ')
        print(m)

