 NLP从入门到不放弃（四）：GloVe
日期：2019-07-09 18:51浏览：18评论：0
一、基础思想

1. LSA(SVD)—基于奇异值分解的潜在语义分析算法—利用了全局特征的矩阵分解方法

2.Word2Vec—利用局部上下文特征（滑窗）（以上参见之前博客）

3.共现矩阵—glove引入共现概率矩阵将全局统计和滑动窗口特征合并。

例如：语料库如下：

• I like deep learning.

• I like NLP.

• I enjoy flying.

```
               共现矩阵：
```

Counts

I

Like

enjoy

deep

Learning

NLP

Flying

I

0

2

1

0

0

0

0

Like

2

0

0

1

0

1

0

Enjoy

1

0

0

0

0

0

1

Deep

0

1

0

0

1

0

0

Learning

0

0

0

1

0

0

0

NLP

0

1

0

0

0

0

0

Flying

0

0

1

0

0

0

0

共现概率矩阵：例如矩阵（0,1）位置的意义是：当i出现的时候，第二个元素是like的概率；需要区分的是，共现矩阵不论出现顺序，共现概率矩阵需要区别先后顺序。

例如dog、bark与puppy、bark的共现概率比值接近1，可以认为dog与puppy具有很强的相关性。这就是GloVe的思想

缺点：面临稀疏性问题、向量维数随词典大小线性增长，若使用svd等降维，计算量也较大。

```
  4.不需要人工标注label，但训练方式和监督学习一致，基于label Log(Xij)。具体实验流程： 

         采用了AdaGrad的梯度下降算法，对矩阵XX中的所有非零元素进行随机采样，学习曲率（learning rate）设为0.05，在vector size小于300的情况下迭代了50次，其他大小的vectors上迭代了100次，直至收敛。最终学习得到的是两个vector是和，因为XX是对称的（symmetric），所以从原理上讲和是也是对称的，他们唯一的区别是初始化的值不一样，而导致最终的值不一样。所以这两者其实是等价的，都可以当成最终的结果来使用。但是为了提高鲁棒性，我们最终会选择两者之和作为最终的vector（两者的初始化不同相当于加了不同的随机噪声，所以能提高鲁棒性）。Context windows size大概在6-10、vector dimension在300时性能最好。
```

二、算法

看到两篇特别好的文章，结合起来看清晰易懂。知乎的这一篇直接贴到了文章里，另一篇csdn的附上链接。

参考链接：https://zhuanlan.zhihu.com/p/42073620

https://blog.csdn.net/coderTC/article/details/73864097

 

https://pic2.zhimg.com/80/v2-33e51493fa8e2170bba8df468e41e685_hd.jpg

https://pic2.zhimg.com/80/v2-11fe585fa53b9e54d94c9c996187bf89_hd.jpg

https://pic4.zhimg.com/80/v2-fef86f8c0487368408f20e453727104b_hd.jpg

三、其他

GloVe与word2vec的区别

word2vec是基于预测的模型，而GloVe是基于统计的模型，本质上是对共现矩阵进行降维。

两个模型在并行化上有一些不同，即GloVe更容易并行化，所以对于较大的训练数据，GloVe更快。

优化

```
     共现矩阵太过稀疏，使用了混合的数据结构存储共现矩阵，当一对词的频数都很高时，共现概率也高，放在左上角，存储在内存中，剩余部分写出最后再汇总。
```

目标

```
     通过训练词向量和上下文向量，能够重构共现矩阵。
```

四、源码

Src包有4个.c的文件，分别是：

1. vocab_count：单词统计，生成vocab.txt（单词 词频）；
2. cooccur：统计词的共现(生成cooccurrence.bin)；
3. shuffle：对共现情况整理(生成cooccurrence.shuf.bin)；
4. glove： glove算法训练模型；

demo.sh源码解析：

CORPUS=wiki-seg.txt  //替换成自己语料

VOCAB_FILE=vocab.txt  //按词频降序排序的词典

COOCCURRENCE_FILE=cooccurrence.bin

COOCCURRENCE_SHUF_FILE=cooccurrence.shuf.bin

BUILDDIR=build  //生成的文件夹名

SAVE_FILE=vectors  //生成的词向量文件的名字

VERBOSE=2

MEMORY=4.0  //内存

VOCAB_MIN_COUNT=5

VECTOR_SIZE=50  //词向量维度

MAX_ITER=15  //训练迭代次数

WINDOW_SIZE=15  //滑窗大小

BINARY=2  //保存文件类型0-只存文本格式 1-只存二进制格式 2-同时保存

NUM_THREADS=8  //线程数

X_MAX=10



