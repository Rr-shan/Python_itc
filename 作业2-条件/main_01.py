
'''
输入整数x,y,z,判断x^3+y^3+z^3和1000的关系

【问题描述】输入整数x,y,z,若x^3+y^3+z^3>1000,则输出x^3+y^3+z^3-1000的结果，否则输出三个数之和。
【输入形式】
用eval()函数结合input()函数同时输入3个整数，输入数字时用逗号分隔
【输出形式】
数字结果
【样例输入】
please input three numbers:1,2,3
【样例输出】
6
'''



x,y,z = eval(input('please input three numbers:'))

sum = pow(x,3)+pow(y,3)+pow(z,3)

print(sum-1000) if sum>1000  else print(x+y+z)
# 行if