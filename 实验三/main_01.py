
'''
求折点

【问题描述】

　　给定n个整数表示一个商店连续n天的销售量。如果某天之前销售量在增长，而后一天销售量减少，则称这一天为折点，反过来如果之前销售量减少而后一天销售量增长，也称这一天为折点。其他的天都不是折点。如下图中，第3天和第6天是折点。
图片2.png
　　给定n个整数a1, a2, …, an表示销售量，请计算出这些天总共有多少个折点。
　　为了减少歧义，我们给定的数据保证：在这n天中相邻两天的销售量总是不同的，即ai-1≠ai。注意，如果两天不相邻，销售量可能相同。
【输入形式】
　　输入的第一行包含一个整数n。
　　第二行包含n个整数，用空格分隔，分别表示a1, a2, …, an。
【输出形式】
　输出一个整数，表示折点出现的数量。
【样例输入】
　　7
　　5 4 1 2 3 6 4
【样例输出】
　　2
       3 low
       6 high
【样例说明】
　　2        2个折点
       3  low    第三天第一个拐点为高到低到高
       6  high    第六天第二个拐点为低到高到低
'''

n = input()
str = input()
ls = str.split(' ')
ls = list(map(int, ls))

sum = 0
low = []
high = []

for i in range(len(ls)):
    if i != 0 and i != len(ls) - 1:
        if ls[i] > ls[i-1] and ls[i] > ls[i+1]:
            high.append(ls.index(ls[i])+1)
            sum += 1
        if ls[i] < ls[i-1] and ls[i] < ls[i+1]:
            low.append(ls.index(ls[i])+1)
            sum += 1

print(sum)
for i in range(len(low)):
    print(low[i],"low")
for i in range(len(high)):
    print(high[i],"high")

# 7
# 5 4 1 2 3 6 4