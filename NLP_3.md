NLP从入门到不放弃（三）：Word2Vec不完全教程
日期：2019-07-08 18:53浏览：14评论：0
参考链接：

https://code.google.com/archive/p/word2vec/

https://blog.csdn.net/u014595019/article/details/51884529



一、一些有趣的小概念：

1. Huffman编码 

a)    按字符出现概率分配码长，可使平均码长最短

b)    Word2Vec将训练预料中的词当作叶子节点，在语料中出现次数当作权值

c)    一个生动的小例子：https://zhuanlan.zhihu.com/p/25181781

2. Softmax 

a)    对向量进行归一化，凸显其中最大的值并抑制远低于最大值的其他分量。即概率与权值有关。

b)   参考链接：https://blog.csdn.net/bitcarmanlee/article/details/82320853

3. 交叉熵

a)    机器学习领域常用，目标函数即为代价函数

b)    参考链接：https://blog.csdn.net/tsyccnh/article/details/79163834

 

二、Word2Vec

word2vec的核心思想就是预测每个单词与其上下文单词之间的关系。它是通过一个嵌入空间使得语义上相似的单词在该空间内距离很近。Embedding其实就是一个映射，将单词从原先所属的空间映射到新的多维空间中，也就是把原先词的所在空间嵌入到一个新的空间中去。

Word2Vec模型实际上分为了两个部分，第一部分为建立模型，第二部分是通过模型获取嵌入词向量。我们真正目标：隐层的权重矩阵。

Word2vec创造一个空间，把词嵌入进去之后，在这个空间计算距离，就可以根据距离判断词之间（词法、语义上）的相似性。

分为两种算法：

·Skip-grams（SG）：给定单词，去预测此词的上下文单词。

·Continuous Bag of Words（CBOW）：从给定的上下文单词，去预测该单词。

1.Skip-grams：

我们的目标是计算在给定单词的条件下，其他单词出现的概率。例如给定窗口大小为2，则要计算前后两个共计4个单词出现的概率。

首先对文档中n个单词形成词汇表后，对词汇表进行one-hot编码，得到n个n维的向量，每个向量仅有一个维度取1，其余为0。

向量与隐层的权重矩阵进行乘法计算后，得到的输出就是每个输入单词的嵌入词向量。输出层是一个softmax回归分类器，每个节点输出一个概率。

```
  参考链接：
```

https://zhuanlan.zhihu.com/p/27234078 理解 Word2Vec 之 Skip-Gram 模型

https://zhuanlan.zhihu.com/p/50243702 Word2Vec原理解析及简单实现

2.CBOW：

CBOW模型的训练输入是某一个特征词的上下文相关的词对应的词向量，而输出就是这特定的一个词的词向量。

3.优化：

1. 将常见的单词组合（word pairs）或者词组作为单个“words”来处理。

2. 对高频次单词进行抽样来减少训练样本的个数。

3. 对优化目标采用“negative sampling”方法，这样每个训练样本的训练只会更新一小部分的模型权重，从而降低计算负担。

   技术细节：

   ```
        https://www.cnblogs.com/peghoty/p/3857839.html
   
        https://www.cnblogs.com/neopenx/p/4571996.html
   ```

4.其他

   语料要求：因为模型训练按行进行，利用特殊词</s>进行分割，最好一个句子放在一行。

```
       用法示例：https://radimrehurek.com/gensim/models/word2vec.html 
```

​           
