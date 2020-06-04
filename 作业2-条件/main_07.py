
'''
适婚问题!

【问题描述】
输入年龄和性别，判断你当前的个人情况！男性小于30岁显示：young，30岁到36岁之间显示：marriageable age，大于36岁显示：old。
女性小于25岁显示：young，25岁到30岁之间显示：marriageable age，大于30岁显示：old。
【样例输入1】
sex(F or M):F
age:28
【样例输出1】
marriageable age
【样例输入2】
sex(F or M):M
age:28
【样例输出2】
young
【样例输入3】
sex(F or M):H
age:28
【样例输出3】
wrong
【样例说明】输入F或f代表女性；M或m代表男性，输入性别有误时提示wrong。考虑用嵌套的if语句来实现。
【评分标准】
'''

s = input('sex(F or M):')
a = eval(input('age:'))

if s == 'F' or s =='f':
    if a<25:
        print('young')
    elif a> 30:
        print('old')
    else:
        print('marriageable age')
elif s == 'M' or s == 'm':
    if a< 30:
        print('young')
    elif a> 36:
        print('old')
    else:
        print('marriageable age')
else:
    print('wrong')