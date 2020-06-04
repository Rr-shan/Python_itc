# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 11:47
# @Author  : Sanzzi


'''
学生成绩转换

【问题描述】读入文件d1.txtd1.txt，每行数据包含两个信息：学号和成绩，将成绩转换成5级制并按照学号递减排序，在屏幕上输出学号和成绩中间有一个空格的间隔，将不及格学生人数写到文件d2.txt中。
【样例输出】
2 D
3 B
4 D
5 A
7 E
8 A
10 C
11 C
14 B
【样例说明】
【评分标准】
'''


with open(r'd1.txt','r',encoding='utf8') as f:
    data = f.readlines()

# find the index
list = []
for i in range(len(data)):
    # print(data[i].split()[0])
    list.append(int(data[i].split()[0]))
# sort
list.sort()
# print(list)

fail_num = 0

# print(fail_num)
for i in list:
    # print(int(i))
    # 已经不是顺着读了！这二者没有联系在一起
    for j in range(len(list)):
        if int(data[j].split()[0]) == i:
            # print(i)
            if int(data[j].split()[1]) < 60:
                print(i, end=' ')
                print('E')
                fail_num += 1
            else:
                flag = 0
                if int(data[j].split()[1]) >= 60 and int(data[j].split()[1]) < 70:
                    flag = 'D'
                elif int(data[j].split()[1]) >= 70 and int(data[j].split()[1]) < 80:
                    flag = 'C'
                elif int(data[j].split()[1]) >= 80 and int(data[j].split()[1]) < 90:
                    flag = 'B'
                else:
                    flag = 'A'
                print(i,end=' ')
                print(flag)

    # print(int(data[i].split()[0]))


# print(fail_num)

with open('d2.txt', 'w', encoding='utf-8') as f:
    f.write(str(fail_num))




# 简化版
# with open(r'd1.txt','r',encoding='utf8') as f:
#     data = f.readlines()
#
# list = []
# for i in range(len(data)):
#     list.append(int(data[i].split()[0]))
# list.sort()
#
# fail_num = 0
#
# for i in list:
#     for j in range(len(list)):
#         if int(data[j].split()[0]) == i:
#             if int(data[j].split()[1]) < 60:
#                 print(i, end=' ')
#                 print('E')
#                 fail_num += 1
#             else:
#                 flag = 0
#                 if int(data[j].split()[1]) >= 60 and int(data[j].split()[1]) < 70:
#                     flag = 'D'
#                 elif int(data[j].split()[1]) >= 70 and int(data[j].split()[1]) < 80:
#                     flag = 'C'
#                 elif int(data[j].split()[1]) >= 80 and int(data[j].split()[1]) < 90:
#                     flag = 'B'
#                 else:
#                     flag = 'A'
#                 print(i,end=' ')
#                 print(flag)
#
# with open('d2.txt', 'w', encoding='utf-8') as f:
#     f.write(str(fail_num))

