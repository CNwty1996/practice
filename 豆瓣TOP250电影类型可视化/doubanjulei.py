from sklearn.feature_extraction.text import CountVectorizer #将文本词转换为词频矩阵
from sklearn.feature_extraction.text import TfidfTransformer #求文本的TF-IDF值
from sklearn.cluster import KMeans #KMeans聚类分析
import matplotlib.pyplot as plt #图库
from sklearn.decomposition import PCA #使用PCA降维

#文本聚类
def julei(file):
    corpus = []
    for line in open(file, 'r', encoding='UTF-8').readlines(): #读取文本中的数据
        corpus.append(line.strip())
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    word = vectorizer.get_feature_names()
    print("文本中包含的词语：")
    for n in range(len(word)):
        print(word[n])

#计算TF-IDF值
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    weight = tfidf.toarray()
    print("词语的TF-IDF值是：")
    print(weight)

#K-Means聚类
    clf = KMeans(n_clusters=4) #分成4个聚类，可调整
    s = clf.fit(weight) #对词频权重进行聚类
    y_pred = clf.fit_predict(weight) #拟合
    print("文本的类簇中心为：")
    print(clf.cluster_centers_) #类簇中心
    print("聚类的距离为：")
    print(clf.inertia_) #距离，评估类簇个数是否合适，越小越好
    print("预测的类标是：")
    print(y_pred) #预测类标

#降维处理
    pca = PCA(n_components=2) #降成二维绘图
    newdata = pca.fit_transform(weight) #将权重降维
    print("降成二维后的数值：")
    print(newdata)
    x = [n[0] for n in newdata]
    y = [n[1] for n in newdata] #向x,y中插入数组数据

#可视化
    plt.scatter(x, y, c=y_pred, s=100, marker='*')
    plt.title("Kmeans")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()