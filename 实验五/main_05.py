
import jieba
import wordcloud
import matplotlib.colors as colors


import imageio
mk = imageio.imread("heart.png")
w = wordcloud.WordCloud(mask=mk)
colormaps = colors.ListedColormap(['#FF0000','#FF7F50','#FFE4C4'])  # 换成自己喜欢的颜色


w = wordcloud.WordCloud(width=1000,
                        height=700,
                        colormap=colormaps,
                        background_color='white',
                        font_path='simkai.ttf',
                        mask=mk,
                        scale=15)

f = open('疫情传播.txt',encoding='gbk')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

string = txt
w.generate(string)

w.to_file('疫情传播.png')




#
# import jieba
# import wordcloud
#
# # 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
# import imageio
# mk = imageio.imread("girl.png")
# w = wordcloud.WordCloud(mask=mk)
#
# # 构建并配置词云对象w，注意要加scale参数，提高清晰度
# w = wordcloud.WordCloud(width=1000,
#                         height=700,
#                         background_color='white',
#                         font_path='simkai.ttf',
#                         mask=mk,
#                         scale=15)
#
# # 对来自外部文件的文本进行中文分词，得到string  ，有可能会遇到编码问题，这个可以根据报错来
# f = open('全宋词全集.txt',encoding='gbk')
# txt = f.read()
# txtlist = jieba.lcut(txt)
# string = " ".join(txtlist)
#
# # 将string变量传入w的generate()方法，给词云输入文字
# w.generate(string)
#
# # 将词云图片导出到当前文件夹
# w.to_file('dd_1.png')