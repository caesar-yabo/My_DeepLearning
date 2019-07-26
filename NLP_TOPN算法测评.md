NLP从入门到不放弃之同义词服务：TOPN算法测评
日期：2019-07-22 19:01浏览：11评论：0
一、背景相关

对于词向量的评测，一般业界使用最广泛的两个评测任务包括相似度任务（word similarity task）和词汇类比任务(word analogy task)，已有github开源项目（参考链接：https://github.com/bamtercelboo/Word_Similarity_and_Word_Analogy）

对于相似度评估，这个任务的目的是评估词向量模型在两个词之间的语义紧密度和相关性的能力，例如男人与女人，男孩与女孩，中国与北京这些词对之间的相似度。

在词相似度任务上，一般采用 斯皮尔曼等级相关系数（ρ）（Spearman's rank correlation coefficient） 作为评价指标，简写为 rho ，它是衡量两个变量的依赖性的指标，它利用单调方程评价两个统计变量的相关性。 如果数据中没有重复值， 并且当两个变量完全单调相关时，斯皮尔曼相关系数则为 +1 或 −1 。对于样本容量为 n 的样本，相关系数 ρ 的计算如下图：

https://i.imgur.com/QOKtcHL.jpg

评价指标计算

1、首先，我们有一个金标文件（wordsim-240.txt），这份文件标注了两个词之间的相似度分数，是由人工标注的，类似于下面：

大学生 就业 7.45
图片 照片 7.45
北京 中国 7.4
能源 石油 7.4
电台 音乐 7.4

2、我们根据词向量计算两个词之间的 余弦值（cos） 作为词的相似度分数，然后计算金标分数与余弦值分数之间的斯皮尔曼相关系数。

3、代码：

def Word_Similarity(self, similarity_name, vec):

```
pred, label, found, notfound = [], [], 0, 0

with open(similarity_name, encoding='utf8') as fr:

   for i, line in enumerate(fr):

       w1, w2, score = line.split()

       if w1 in vec and w2 in vec:

          found += 1

          pred.append(self.cos(vec[w1], vec[w2]))

          label.append(float(score))

       else:

          notfound += 1

file_name = similarity_name[similarity_name.rfind("/") + 1:].replace(".txt", "")

self.result[file_name] = (found, notfound, self.rho(label, pred))
```

二、具体测评

```
     目前在synonyms的框架上进行修改，针对两个方面做了测评，一块是加载时间和运行时间，一块是近义词的准确度。分别上图。
```

加载时间（top1)

平均运行时间（top1)

加载时间（top3)

平均运行时间（top3)

加载时间（top5)

平均运行时间（top5)

加载时间（top10)

平均运行时间（top10)

kd树

66.38s

0.332s

66.94s

1.297s

68s

1.353s

67.72s

1.462s

ball树

67.08s

0.9440s

66.8s

1.074s

66.97s

1.078s

66.94s

1.0799s

表一

 

 

各种算法加载数据占用内存（MB）
syno占用内存	wiki占用内存
kd树	542.203125MB	2953.89453125MB
ball树	518.53112MB	2604.00390625MB                                               表二



Kd-tree 基于自己训练的wiki词向量top10近义词

 



Ball-tree基于synonyms自带词向量的top10近义词

```
     还做了基于annoys的实验，大概能得出的结论是：

     1.当使用同一词向量时，加载速度annoys>>kd-tree>ball-tree，annoys加载时间长，占用内存大，可以选择第一次构建后保存在本地，二次加载占用内存会略小一点，此处详细数据尚待补充；

     2.kd-tree和ball-tree的准确度完全一致，在正常情况下，ball-tree的加载时间和运行时间都要略小于kd-tree一点点，属于肉眼不可见的改善，ball-tree加载占用的内存也略小；

     3.synonyms自带的词向量质量优于我们的词向量，然鹅annoys在我们自己训练的词向量上，效果与synonyms自带词向量在kd-tree上效果近似，大概近义词质量可以这么排序：
```

Synonyms自带词向量在kd-tree和ball-tree~=自训wiki词向量在annoys上>自训词向量在kd-tree和ball-tree；


目前还在试验阶段，接下来想要测试的是：具体占用内存情况；annoys运行时间加载时间和基于synonyms自带词向量的近义词质量；基于腾讯880w词向量的各项数据。应该这些做完就可以得到结论了~

     目前有一个疑问需要深入研究一下原理解决：在搜索k近邻时，top10的结果前5并不是top5的结果…这个感觉很奇怪，而且是普遍现象。目前准备8.01进行实习转正答辩吧，不确定是否在这之前有时间解决这个问题，如果来不及就等到答辩完再来补充这一块吧~
