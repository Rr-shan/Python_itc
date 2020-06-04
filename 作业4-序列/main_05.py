
'''
高校类型统计

【问题描述】列表 ls 中存储了我国 39 所 985 高校所对应的学校类型，请以这个列表为数据变量，编写 代码，统计输出各类型的数量，要求按类别字母顺序输出。
ls = ["Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", "Comprehensive", \
      "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive",\
      "Normal", "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \
      "Comprehensive", "Comprehensive", "Comprehensive","Polytechnic",\
      "Polytechnic", "Polytechnic", "Polytechnic", "Normal", "Comprehensive", \
      "Agricultural and Forestry", "Polytechnic", "Comprehensive", "Polytechnic", "Polytechnic", \
      "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \
      "Polytechnic", "Agricultural and Forestry", "Nationalities", "Military"]
【样例输入】
无
【样例输出】
Agricultural and Forestry 2
Comprehensive 20
Military 1
Nationalities 1
Normal 2
Polytechnic 13
'''

ls = ["Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", "Comprehensive", \
      "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive", "Comprehensive",\
      "Normal", "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \
      "Comprehensive", "Comprehensive", "Comprehensive","Polytechnic",\
      "Polytechnic", "Polytechnic", "Polytechnic", "Normal", "Comprehensive", \
      "Agricultural and Forestry", "Polytechnic", "Comprehensive", "Polytechnic", "Polytechnic", \
      "Polytechnic", "Comprehensive", "Polytechnic", "Comprehensive", "Comprehensive", \
      "Polytechnic", "Agricultural and Forestry", "Nationalities", "Military"]

num = ['Agricultural and Forestry','Comprehensive','Military','Nationalities','Normal','Polytechnic']

for i in range(6):
    print(num[i]+" "+str(ls.count(num[i])))
