NLP从入门到不放弃（七）：词向量评价相关及OOV解决方案
日期：2019-07-20 11:45浏览：6评论：0
一、词向量评价

1.皮尔逊相关系数

```
     https://pic1.zhimg.com/80/v2-71de3ac89fb7e62a24eae9bdbb56aa8d_hd.jpg
```

Cos之前两个向量先进行中心化，中心化的意思是说, 对每个向量, 我先计算所有元素的平均值avg, 然后向量中每个维度的值都减去这个avg, 得到的这个向量叫做被中心化的向量. 机器学习, 数据挖掘要计算向量余弦相似度的时候, 由于向量经常在某个维度上有数据的缺失, 预处理阶段都要对所有维度的数值进行中心化处理。

 

2.评估方法

考虑单词间的语义关系-intrinsic task，例如同义词，例如国家与首都的关系，而不放到具体语境中，是比较容易进行评估的；extrinsci task是下游的各种NLP具体任务，两者的相关性并不大，因此语义评估的结果对于下游任务没有太多指导意义。对于下游任务，当增大维度不能提高性能时，将多个不同上下文习得的word vectors拼起来会提升性能。

 

3.评估指标：

1.Relatedness：相似度评价指标，看空间距离近的词是否和人的直觉一致，目前大部分工作依赖wordsim353（英文）等词汇相似性数据集进行相关性度量，并作为评价标准。对数据集的大小、领域敏感。

2.Analogy：著名的king-queen=man-woman

3.Categorization：看词在每个分类中的概率

4.聚类算法

5.可解释性

4.可用数据集

```
1.同义词词林

2.how-net 知网

3.wordsim-240、wordsim-297

4.在线查找同义词（通过数据抓取）
```

参考链接：https://www.zhihu.com/question/37489735/answer/73026156

中文测试数据集：https://github.com/CallMeJiaGu/WordSimilarityAnalogyData

哈工大同义词词林：https://www.ltp-cloud.com/download/#down_cilin无法打开

在线查找：https://www.cilin.org/jyc/

http://jyc.5156edu.com/

https://chinese.abcthesaurus.com/

知网：http://www.keenage.com/html/c_index.html

参考：https://www.cnblogs.com/bymo/p/8440722.html

 

二、中文词向量训练及oov现象解决方案

1.汉字的部首和非部首都蕴含很多信息，为了帮助计算机更好的理解汉字，甚至不给定文本的时候也可以通过这些部分推断汉字意义。

2.默认以word为词，character为字，一个词的语义不仅可以从上下文获得，也可以从构成这个词的汉字中推断出。

```
困难：与词相比，汉字拥有的意思更多。一个汉字在不同词中，可能有不同的语义。因此, 一个汉字对应一个 character embedding 是不够的；不是所有词都能用汉字意思的语义结合来表意。尤其是音译的词, 比如巧克力可以说巧, 克, 力没有半毛钱关系, 此时仍然用上述方法反而是有害的。
```

可采用的策略是：

使用 multiple-prototype character embedding，即为一个汉字分配多个 character embedding，以表示它的不同意思；

简单粗暴地创建 non-compositional words (多个汉字组合成词的过程被称为 compose) 列表, 只使用他们的 word embedding.

position-based character embeddings, 针对 character 在 word 中的位置为其分配向量, 分为 3 种情况: 词头, 词中和词尾. 具体地说, 能力和智能中的能用不同的向量表示.cluster-based character embeddings, 对 character 所有出现的情况做聚类, 为每个聚类分配一个向量.可以对 position-based character embeddings 再做聚类, 即更细分了, 称为 position-cluster-based character.nonparameters cluster-based character embeddings, 上面的聚类方法具有固定的类数, 而无参聚类方法能为 characters 分配不同数量的聚类, 聚类数在训练时习得, 更灵活.

3.oov处理方法

数量不多，可以当成unk处理

```
思路1：把训练集中所有出现频率小于某个阈值的词都标记为UNK，当然也别太多，这样就得到了UNK的embedding，这里的embedding有一定的语义信息；

思路2：
```

a. 把UNK都初始化成0的向量

b.每次都把UNK初始化成一个新的随机向量

c.把所有oov词拆成字符，优点消除所有oov，缺点文本序列非常长

d.英文：把所有词拆成sub-word，character n-gram

e.扩大词表

参考链接：https://juejin.im/entry/5a6af990f265da3e283a3b42
