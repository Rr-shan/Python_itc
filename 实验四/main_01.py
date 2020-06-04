
'''
Z字形扫描

【问题描述】
　　在图像编码的算法中，需要将一个给定的方形矩阵进行Z字形扫描(Zigzag Scan)。给定一个n×n的矩阵，Z字形扫描的过程如下图所示：
　　 图片1.png
　　对于下面的4×4的矩阵，
　　1 5 3 9
　　3 7 5 6
　　9 4 6 4
　　7 3 1 3
　　对其进行Z字形扫描后得到长度为16的序列：
　　1 5 3 9 7 3 9 5 4 7 3 6 6 4 1 3
　　请实现一个Z字形扫描的程序，给定一个n×n的矩阵，输出对这个矩阵进行Z字形扫描的结果。
【输入形式】
　　输入的第一行包含一个整数n，表示矩阵的大小。
　　输入的第二行到第n+1行每行包含n个正整数，由空格分隔，表示给定的矩阵。
【输出形式】
　　输出一行，包含n×n个整数，由空格分隔，表示输入的矩阵经过Z字形扫描后的结果。
【样例输入】
　　4
　　1 5 3 9
　　3 7 5 6
　　9 4 6 4
　　7 3 1 3
【样例输出】
1 5 3 9 7 3 9 5 4 7 3 6 6 4 1 3
'''


n=int(input())
info=[]

v_list=[[0,1],[1,-1],[1,0],[-1,1],[0,1]]

for i in range(n):
	info1=list(map(int,input().split()))
	info.append(info1)

num_list=[[0]*n for i in range(n)]

num=0
v=[0,1]
i=0
j=0
end_list=[]

def v_find(v1):
	loc = v_list.index(v1)+1
	return v_list[loc]

def num_get(i1,j1,v1):
	if (i1+v1[0]<n)and(j1+v1[1]<n)and(i1+v1[0]>=0)and(j1+v1[1]>=0)and(num_list[i1+v1[0]][j1+v1[1]]!=1):
		global i
		i= i1+v1[0]
		global j
		j=j1+v1[1]
		if v1==v_list[0]:
			v1=v_list[1]
		if v1==v_list[2]:
			v1=v_list[3]
		global v
		v=v1
		return info[i][j]
	else:
		return num_get(i,j,v_find(v1))

for h in range(n*n):
	if h==0:
		num=info[0][0]
		end_list.append(num)
	else:
		num_list[i][j]=1
		end_list.append(num_get(i,j,v))

# 输出
for i in range(len(end_list)):
	if i==len(end_list)-1:
		print(end_list[i])
	else:
		print(end_list[i],end=" ")


