
'''
输出斐波拉契数列

【问题描述】
斐波那契数列指的是这样一个数列：
1，1，2，3，5，8，13，21，34，55，89，144，233，377，610，987，1597，2584...
这个数列从第3项开始，每一项都等于前两项之和。
定义一个函数fib()，给定n，返回n以内的斐波那契数列。
【输入形式】
输入一个大于3的整数n
【输出形式】
输出n以内的斐波那契数列
【样例输入】
Please input a number:200
【样例输出】
1,1,2,3,5,8,13,21,34,55,89,144,
'''

n = eval(input('Please input a number:'))

def fib(n):
    a1 = 1
    a2 = 1
    print(a1,end=',')
    print(a2,end=',')
    for an in range(2,n+1):
        if an == a1 + a2 :
            print(an,end=',')
            a1 = a2
            a2 = an

fib(n)