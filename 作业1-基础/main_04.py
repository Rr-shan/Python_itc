# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 8:54
# @Author  : Sanzzi

'''
温度转换程序

【问题描述】在温度刻画的不同体系中，摄氏度以1标准大气压下水的结冰点为0度，沸点为100度。华氏度以1标准大气压下水的结冰点为32度，沸点为212度。如何利用程序辅助进行摄氏度和华氏度之间的转换，结果保留1位小数。
设计算法：根据华氏和摄氏温度定义，其单位刻度对应温度关系为(212-32)/(100-0)=1.8，转换公式如下：
  C = ( F – 32 ) / 1.8
  F = C * 1.8 + 32
【输入形式】输入温度加温度制式的代表字母，摄氏温度对应字符是c或C，华氏温度对应字符是f或F
【输出形式】转换后的温度加温度制式的代表字母
【样例输入输出1】
What is the temperature?82F
The converted temperature is 27.8C
【样例输入输出2】
What is the temperature?28C(有下划线)
The converted temperature is 82.4F
【样例说明】下划线表示输入，结果保留1位小数
【评分标准】
'''

val = input('What is the temperature?')

if val[-1] in ['f','F']:
    c = (float(val[0:-1]) - 32)/1.8
    print('The converted temperature is %.1fC'%c)
elif val[-1] in ['c','C']:
    f = float(val[0:-1])*1.8 +32
    print('The converted temperature is %.1fF'%f)
else:
    print('input error!')