
'''
找不同

【问题描述】
          9个同学一起做游戏，每个人报一个[1,20]区间上的正整数，请你编程求出有多少个不同的数。
【输入形式】
        输入1行，输入9个[1,20]区间上的整数，每个整数之间以空格为分隔符
【输出形式】
        输出1个数，表示输入的9个数中不同数的个数。
【样例输入】
        1 2 3 3 2 2 7 8 9
【样例输出】
        6
【样例说明】
【评分标准】
'''

str = input()
ls = str.split(' ')
ls = list(set(ls))

print(len(ls))
