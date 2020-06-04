# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 11:47
# @Author  : Sanzzi

'''
电影选看

【问题描述】
    在当前目录下有一个文件名为movie.txt，文件中有6列数据，包括No Name Year Country Score Lasting，分别表示序号、电影名、上映年份、国家、评分和电影时长。李华只想观看时长在90分钟以下（包括90分钟）的电影。请你编写程序帮他挑选出符合条件的电影序号。一行打印一个序号写到文件out.txt中。
    鼠标右击以下文件，选择“另存为”把文件保存至本地硬盘中。
        movie.txt
【样例输入】
无
【样例输出】
6
7
8
9
后面还有很多就不列出来了
'''


with open(r'movie.txt','r',encoding='utf8') as f:
    data = f.readlines()
    # data = [d.strip() for d in f.readlines()]
    # data = [d.strip(r'\t') for d in f.readlines()]
    # print(int(data[6][-4:])) # 1008

# print(data[293][-4:]) # 读到了294

with open('out.txt', 'w', encoding='utf-8') as f:
    for i in range(1,len(data)):
        # print(i)
        # print(int(data[i][-4:]))

        # print(data[i].split()[5])

        if int(data[i].split()[5]) <= 90:
            f.write(data[i].split()[0] + '\n')

        # 这个总是不过关
        # if int(data[i][-4:]) <= 90:
        #     if i >= 285:
        #         f.write(str(i+1)+'\n')
        #     else:
        #         f.write(str(i) + '\n')


# 查看整体数据
# filename = 'movie.txt'
# f = open(filename,'r',encoding='utf8')
# data = f.read()
# print(data)



# 简化版本
# with open(r'movie.txt','r',encoding='utf8') as f:
#     data = f.readlines()
#
# with open('out.txt', 'w', encoding='utf-8') as f:
#     for i in range(1,len(data)):
#
#         if int(data[i].split()[5]) <= 90:
#             f.write(data[i].split()[0] + '\n')