
'''
字母计数

【问题描述】
输入字符串，输出字符串中出现次数最多的字母及其出现次数。如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。
【输入形式】
一个字符串。
【输出形式】
出现次数最多的字母及其出现次数
【样例输入】
abcccd
【样例输出】
c 3
'''

str = input()


def countchar(str):
    array = list(str)
    max_num = array.count(max(array, key=array.count))
    for i in sorted(set(array)):
        if array.count(i) == max_num:
            print(i,end=' ')
            print(max_num)
countchar(str)