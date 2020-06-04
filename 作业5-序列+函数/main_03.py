
'''
一年中第几天

【问题描述】
     输入某年某月某日，判断这一天是这一年的第几天？程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天。特殊情况：闰年且输入月份大于3时需考虑多加一天。

提示：(1) 闰年的2月有29天，平年的2月有28天；
      (2) 如果年份满足以下两个条件之一，则该年就是闰年。
         i) 年份能被4整除且不能被100整除
         ii) 年份能被400整除
【输入形式】
输入一行，一行三个整数，用空格隔开，分别代表年月日。如2012 2 7
代表2012年2月7日。注意，不要输入任何汉字。
【输出形式】
输出只有一个数字，即所对应的日期是该年的第几天。
【样例输入】
2012 1 1
【样例输出】
1
'''

mon_01 = [31,28,31,30,31,30,31,31,30,31,30,31]
mon_02 = [31,29,31,30,31,30,31,31,30,31,30,31]

d = input()
ls = d.split(' ')
year = int(ls[0])
mon = int(ls[1])
date = int(ls[2])

def isLeapYear(year):
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        return True
    else:
        return False

def summarydays(year,mon,date):
    sum = 0
    if isLeapYear(year):
        for i in range(mon-1):
            sum += mon_02[i]
        return sum + date
    else:
        for i in range(mon-1):
            sum += mon_01[i]
        return sum + date

print(summarydays(year,mon,date))