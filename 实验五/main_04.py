
import jieba

txt = open("红楼梦.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
#排除一些不是人名的词语
excludes=['什么','一个','我们','那里','如今','你们','说道','知道','起来','姑娘','这里','出来','他们','众人','奶奶','自己','一面'
          ,'只见','怎么','两个','没有','不是','不知','听见','这个','这样','进来','咱们','就是','东西','告诉','回来','只是','大家',
          '只得','这些','不敢','出去','所以','不过','不好','的话','一时','过来','不能','心里','今日','姐姐','太太','丫头','银子',
          '如此','二人','几个','答应','这么','还有','只管','一回','说话','那边','外头','这话','打发','自然','罢了','今儿','屋里','-----------------------']
counts = {}
for word in words:
      if len(word) == 1:   #排除单个字符的分词结果
          continue
      else:
          counts[word] = counts.get(word,0) + 1

for word in excludes:
      del(counts[word])

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(20):
      word,count = items[i]
      print("{0:<10}{1:>5}".format(word,count))


######################################################


# 红楼梦人物出场统计
# import jieba
#
# txt = open("红楼梦.txt", "r", encoding='utf-8').read()  # 打开文档
# # 排除干扰词
# excludes = {"什么", "一个", "我们", "那里", "你们", "如今", "知道", "起来", "说道",
#             "姑娘", "这里", "出来", "他们", "众人", "奶奶", "自己", "一面", "只见",
#             "怎么", "两个", "没有", "不是", "不知", "这个", "听见", "这样", "进来",
#             "咱们", "告诉", "就是", "东西", "回来", "只是", "大家", "老爷", "只得",
#             "丫头", "这些", "不敢", "出去", "所以", "不过", "的话", "不好", "姐姐",
#             "一时", "不能", "过来", "心里", "二爷", "如此", "今日", "银子", "几个",
#             "答应", "二人", "还有", "只管", "这么", "说话", "一回", "那边", "这话",
#             "外头", "打发", "自然", "今儿", "罢了", "屋里", "那些", "听说", "小丫头",
#             "如何", "问道", "看见", "妹妹", "人家", "不用", "媳妇"}
# words = jieba.lcut(txt)
# counts = {}
# for word in words:
#
#     if len(word) == 1:  # 排除单个字符
#         continue
#     elif word == "王夫人" or word == "太太":  # 同一人物整合处理
#         rword = "王夫人"
#     elif word == "贾母" or word == "老太太":
#         rword = "贾母"
#     elif word == "凤姐" or word == "凤姐儿":
#         rword = "凤姐"
#     elif word == "黛玉" or word == "林黛玉":
#         rword = "黛玉"
#     else:
#         rword = word
#     counts[rword] = counts.get(rword, 0) + 1
# for word in excludes:
#     del (counts[word])
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(20):
#     word, count = items[i]
#     print("{0:<10}{1:>5}".format(word, count))
