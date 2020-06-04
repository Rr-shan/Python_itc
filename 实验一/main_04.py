
'''
	录取研究生

【问题描述】某高校录取研究生的要求是，每门课成绩不低于60分，总成绩不低于340分，370分以下为自费。编一程序实现输入一个学生的四门课成绩，试判断该生为该校录取的情况（没有录取“not”、自费“pay”、公费“free”三种情况）。
【输入形式】
输入四门课的成绩，成绩均为0~150之间的整数。输入4门课成绩的时候可以结合eval()和input()函数一次性输入4个值，输入数字时用逗号分隔
【输出形式】
not或者pay或者free
【样例输入】
four scores:55,120,110,120
【样例输出】
not
【样例说明】
【评分标准】
'''

a,b,c,d = eval(input('four scores:'))
grades_sum = a+b+c+d
flag = not (a>=60 and b>=60 and c>=60 and d>=60)

if grades_sum<340 or flag:
    print('not')
elif grades_sum<370:
    print('pay')
else:
    print('free')

