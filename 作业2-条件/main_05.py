
'''
判断三角形，并判断是何种三角形

【问题描述】输入三个数，判断它们能否构成一个三角形。若能，则输出三角形是等边三角形、直角三角形，还是普通三角形；若不能，则输出“不能组成三角形”提示信息。
【输入形式】
输入3条边长的时候可以结合eval()和input()函数一次性输入3个值，输入数字时用逗号分隔
【输出形式】
false或者equilateral triangle或者right triangle或者ordinary triangle
【样例输入】
please input three numbers:3,4,5
【样例输出】
right triangle
【样例说明】
【评分标准】
'''

x,y,z = eval(input('please input three numbers:'))

if not (x+y>z and x+z>y and z+y>x) :
    print('false')
elif x*x + y*y == z*z or x*x + z*z == y*y or y*y + z*z == x*x:
    print('right triangle')
elif x == y == z :
    print('equilateral triangle')
else:
    print('ordinary triangle')

