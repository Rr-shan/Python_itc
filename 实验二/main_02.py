
'''
11整除

【问题描述】
1. 有如下结论：如果一个整数的奇数位上的数字之和与偶数位上的数字之和的差能被11整除，那么这个数能被11整除；(注：每个整数从个位开始计算位数；以123456为例，奇数位之和为6+4+2=12，偶数位之和为5+3+1=9)
请利用上述结论，任意给出一个6位整数，输出其奇数位上数字之和，偶数位上数字之和，并判断其能否被11整数。
【输入形式】
输入一个6位的正整数；
【输出形式】
按顺序输出一个奇数位之和、偶数位之和，输出最终的判断能否被11整除；
【样例输入】
 Please input a 6-digital integer:654321
【样例输出】
9
12
FALSE
【样例说明】
【评分标准】
'''


def divide():
    n = eval(input('Please input a 6-digital integer:'))
    num = str(n)
    sum_one = 0
    sum_two = 0

    for i in range(0,6,2):
        sum_one += int(num[i])
    for i in range(1,6,2):
        sum_two += int(num[i])

    print(sum_two)
    print(sum_one)

    if (sum_one - sum_two) / 11 == 0:
        print('TRUE')
    else:
        print('FALSE')

divide()