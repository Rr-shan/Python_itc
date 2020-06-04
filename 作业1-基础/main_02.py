# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 8:54
# @Author  : Sanzzi

'''
计算圆周长和圆面积

【问题描述】输入圆的半径r,计算圆周长和圆面积，保留2位小数
【输入形式】
Please enter radium:

【输出形式】
【样例输入输出】
  Please enter radium: 10
  Circumference is 62.83
  Round area is 314.16

【样例说明】
注意：圆周率取math库中的常数量pi，另外输出用%f，保留2位小数
import math
后面就可以用math.pi来调用数学库里面的圆周率数值了
'''

import math

r = eval(input('Please enter radium:'))

c = 2*r*math.pi
s = r*r*math.pi

print('Circumference is %.2f'%c)
print('Round area is %.2f'%s)
