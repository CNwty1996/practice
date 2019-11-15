import doubanclaw
import doubancitu
import doubanjulei
import os

if __name__ == '__main__':
    i = 0 #计数器
    file = 'doubanTOP250.txt' #在项目根目录创建，否则需要添加绝对路径
    f = open(file, 'w+', encoding='UTF-8') #若没有该文本，则创建
    f.write("")  #若文本内有内容，则清空
    while i < 10:
        num = i*25
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        doubanclaw.crawl(url,file)
        i += 1
    doubancitu.fenci(file)
    doubanjulei.julei(file)