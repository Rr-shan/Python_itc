
'''
求多项式的和

【问题描述】
  编写一个函数mySum(a,n)，求以下n项式的和：
      s=a+aa+aaa+......+aa...a，  其中a是1~9的数字，最后一项是n位都是a的数字
     程序部分代码如下：
   x,y=eval(input())
   print(mySum(x,y))
  【输入形式】
  输入a和n的值
【输出形式】
  输出s
【样例输入】
  1,5
【样例输出】
  12345
'''

x,y = eval(input())


def mySum(x,y):
    sum = x
    s = x
    k = x
    for i in range(y-1):
        s = s*10 + k
        sum += s
    return sum

print(mySum(x,y))

