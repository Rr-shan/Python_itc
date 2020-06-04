
'''
电话号码

【问题描述】假设电话号码的模式为：3个数字，一个短横线，4个数字，一个短横线和4个数字。如：186-7123-4567。编写程序，用以检查输入的字符串是否匹配电话号码模式，若匹配返回True，否则返回False。
【样例输入】
186-7123-4567
【样例输出】
True
【样例输入】
186--123-4567
【样例输出】
False
'''

num = input()

if num[:3].isdigit() and num[4:8].isdigit() and num[9:13].isdigit() and num[3] == '-' and num[8] =='-' :
    print('True')
else:
    print('False')