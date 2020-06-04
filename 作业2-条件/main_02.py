
'''
统计字符串中非英文字母个数

【问题描述】统计字符串s中非英文字母的个数并输出。
【输入形式】字符串s
【输出形式】非英文字母的个数
【输入示例】a1b2
【输出示例】2
'''

x = input()
count = 0

for i in x:
    if(i>'z' or i<'a'):
        count+=1
    
print(count)
