import urllib.request #url请求
from bs4 import BeautifulSoup #BeautifulSoup爬虫库
import urllib.error #错误索引库

#爬虫函数(带请求头),同时进行存储，获取豆瓣TOP250电影的类型数据
def crawl(url,file):
    try:
        headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/78.0.3904.97 Safari/537.36')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers] #设置网页的请求头
        html = opener.open(url) #打开网页
        bs = BeautifulSoup(html, 'html.parser') #创建本地soup对象
        for tag in bs.find_all(attrs={"class": "item"}): #attrs为绝对查询
            detail = tag.find(attrs={'class': 'bd'})
            micro = detail.find(attrs={'class': ''}).get_text() #获取文本，本例获取的是电影的导演，演员，拍摄日期和类型
            leixing = micro.strip().split('/') #将所得到的数据
            temporary = leixing[-1] #获取列表最后一位的内容
            f = open(file, 'a', encoding='UTF-8') #打开文件，追加模式，编码为UTF-8
            f.write(temporary + '\n') #写入
            f.close()
            print("录入成功！")

    except urllib.error.HTTPError as reason:
        print(reason)