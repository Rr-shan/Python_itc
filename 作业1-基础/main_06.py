# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 8:55
# @Author  : Sanzzi


'''
数字英文形式转换

【问题描述】
阿拉伯数字和英文字母的转换
【输入形式
输入123
【输出形式】
输出对应的bcd
【样例输入】
0123456789
【样例输出】
abcdefghij
【样例说明】
【评分标准】
'''


template = "abcdefghij"
a = input()
for x in a:
    print(template[eval(x)],end='')
