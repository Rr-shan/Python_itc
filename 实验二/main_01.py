
'''
求矩阵两对角线之和

【问题描述】求4*4矩阵两对角线之和。第一行全1，第二行全2，第三行全3，第四行全4
【输入形式】无输入
【输出形式】20
'''

import numpy as np

def countt():
    a1 = np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])
    a1.shape = 4,4
    # x = np.array([(1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4)])
    count = np.sum(a1.diagonal())
    print(count*2)

countt()


# a1 = [1,1,1,1]
# a2 = [2,2,2,2]
# a3 = [3,3,3,3]
# a4 = [4,4,4,4]
#
# a1 = [1 for i in range(4)]
# a2 = [2 for i in range(4)]
# a3 = [3 for i in range(4)]
# a4 = [4 for i in range(4)]
#
# sum = a1[0] + a2[1] +a3[2] + a4[3] + a1[3] + a2[2] + a3[1] + a4[0]
# print(sum)


# import numpy as np
#
# a = np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])
# a.shape = 4,4
#
# # 这个是由元组转化而成的
# x = np.array([(1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4)])
# count = np.sum(a.diagonal())
# print(count*2)