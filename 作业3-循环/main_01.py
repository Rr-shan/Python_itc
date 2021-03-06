
'''
循环编程题

【问题描述】
 已知y=1+1/3+1/5+…+1/2n-1：
求y<3时的最大n值以及最大n值对应的y值(y值保留小数点后2位)。
【样例输入】
无
【样例输出】
n=XXX,y=X.XX
【样例说明】
X代表求出的数。
【评分标准】
用循环完成，直接输出不得分。
'''

y = 0
n = 1

while y<3:
    y += 1/(2*n-1)
    n += 1
else: #
    y -= 1/(2*n-1)
    n -= 1
n -= 1
print("n=%d,y=%.2f"%(n,y))