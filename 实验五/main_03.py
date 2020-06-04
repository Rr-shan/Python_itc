# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 11:47
# @Author  : Sanzzi

'''
武汉气温

【问题描述】
在当前目录下有一个文件名为temp.txt(文件中数据如下:)的文件，存放着武汉从2018年11月10日（周六）到11月19日（周一）间十天的最高和最低气温（单位为摄氏度）。其中，第一行为最高气温，第二行为最低气温。
temp.txt文件中数据:temp.txt
        18,16,16,16,16,19,19,16,11,9
        9,8,11,9,9,10,11,7,4,4
    (1)编程，找出这十天中第几天最热？最高多少度？这十天中第几天最冷？最冷多少度？
   (2)求出这十天的平均气温（这十天日平均温度的平均值，用int()函数取整数）。假设在气象意义上，入冬标准是有5天日均气温低于10℃，根据这十天的气象数据是否能判断武汉已经入冬？(如果入冬,输出In winter;否则输出Not in winter)
【样例输入】
无
【样例输出】
[6, 7]:hot,temperature:19C
[9, 10]:cold,temperature:4C
aver:11
Not in winter
'''


with open(r'temp.txt','r',encoding='utf8') as f:
    data = f.readlines()

high = data[0]
high = high.strip() # 去除 \n
high = high.split(',')
high = list(map(int, high))
# print(high)

low = data[1]
low = low.split(',')
low = list(map(int, low))
# print(low)

mmax = max(high)
# print(mmax)
mmin =min(low)
# print(mmin)

day = [1,2,3,4,5,6,7,8,9,10]
high_day = []
low_day = []

for i in range(len(high)):
    if high[i] == mmax:
        high_day.append(day[i])

print(high_day,end='')
print(':hot,temperature:',end='')
print(mmax,end='')
print('C')

for i in range(len(low)):
    if low[i] == mmin:
        low_day.append(day[i])

print(low_day,end='')
print(':cold,temperature:',end='')
print(mmin,end='')
print('C')

average = 0
for i in high:
    average += i
for i in low:
    average += i

print('aver:',end='')
print(int(average/20))

aver_temp = []
for i in range(len(high)):
    aver_temp.append(int((high[i]+low[i])/2))

# print(aver_temp)
flag = 0
for i in aver_temp:
    if i < 10:
        flag += 1

if flag >= 5:
    print('In winter')
else:
    print('Not in winter')


    ################

with open(r'temp.txt','r',encoding='utf8') as f:
    data = f.readlines()

high = data[0]
high = high.strip()
high = high.split(',')
high = list(map(int, high))

low = data[1]
low = low.split(',')
low = list(map(int, low))

mmax = max(high)
mmin =min(low)

day = [1,2,3,4,5,6,7,8,9,10]
high_day = []
low_day = []

for i in range(len(high)):
    if high[i] == mmax:
        high_day.append(day[i])

print(high_day,end='')
print(':hot,temperature:',end='')
print(mmax,end='')
print('C')

for i in range(len(low)):
    if low[i] == mmin:
        low_day.append(day[i])

print(low_day,end='')
print(':cold,temperature:',end='')
print(mmin,end='')
print('C')

average = 0
for i in high:
    average += i
for i in low:
    average += i

print('aver:',end='')
print(int(average/20))

aver_temp = []
for i in range(len(high)):
    aver_temp.append(int((high[i]+low[i])/2))

flag = 0
for i in aver_temp:
    if i < 10:
        flag += 1

if flag >= 5:
    print('In winter')
else:
    print('Not in winter')