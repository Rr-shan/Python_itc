
'''
	骑车还是走路

【问题描述】
在华农校园里，没有自行车，上课办事会很不方便。但实际上，并非去办任何事情都是骑车快，因为骑车总要找车、开锁、停车、锁车等，这要耽误一些时间。假设找到自行车，开锁并骑上自行车的时间为30秒；停车锁车的时间为20秒；步行每秒行走2米，骑车每秒行走4米。请判断走不同的距离去办事，是骑车快还是走路快。
若一次办事要行走的距离为整数，单位为米。对输入的整数，如果骑车快，输出一行“Bike”；如果走路快，输出一行“Walk”；如果一样快，输出一行“All”。
【输入形式】
输入一个正整数
【输出形式】
Bike或者Walk或者All
【样例输入】
Please input a number of distance:40
【样例输出】
Walk
【样例输入】
Please input a number of distance:200
【样例输出】
All
【样例说明】
样例输入中的下划线表示具体输入的数字
【评分标准】
'''

distance = int(input("Please input a number of distance:"))

tbike = distance/4 + 50
twalk = distance/2

if tbike < twalk:
    print("Bike")
elif twalk < tbike:
    print("Walk")
else:
    print("All")
