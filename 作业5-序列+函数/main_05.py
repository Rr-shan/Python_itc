
'''
奇数之和

【问题描述】
将1～p之间奇数顺序累加存入n中，直到其和首次等于或大于q为止或1～p之间所有奇数参与累加为止。程序输入p,q的值，输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数（分别占一行）。
【输入形式】
用两个input()函数输入p和q的值作为实参，调用自定义函数oddNumSum()实现所述功能
【输出形式】
依次输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数
【样例输入】
1000
4000
【样例输出】
4096
64
127
'''

p = int(input())
q = int(input())

# 只有p是偶数的时候才行

# p = 1000
# q = 4000

def oddNumSum(p,q):
    sum = 0
    k = 0
    for i in range(1,p,2):
        sum += i
        k += 1
        if sum >= q:
            print(sum)
            print(k)
            print(i)
            return

    print(sum+p) # 这是因为忘了
    print(int(p/2) + 1)
    if p%2 == 0:
        print(p-1)
    else:
        print(p)


oddNumSum(p,q)