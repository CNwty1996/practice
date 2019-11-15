import jieba #切词库
import matplotlib.pyplot as plt
from wordcloud import WordCloud #词图库

#使用Jieba切词，并生成词云，词的大小表示出现频率，相同颜色为同一类
def fenci(file):
    text = open(file, encoding='UTF-8').read()
    wordlist = jieba.cut(text, cut_all=True) #使用jieba对文本中词语进行切割
    wl_space_split = " ".join(wordlist)
    my_wordcloud = WordCloud(background_color='white',
                             max_words=500, random_state=40
                             ).generate(wl_space_split) #背景为白，最大出现词语数为500，最多为40个类
    plt.imshow(my_wordcloud) #展示
    plt.axis("off") #不显示角标
    plt.show() #展示