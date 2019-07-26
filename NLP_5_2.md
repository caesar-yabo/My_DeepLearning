NLP从入门到不放弃（五）：ELMo（下）
日期：2019-07-16 19:57浏览：15评论：0
1.原理

编码encode将一个句子转化为word-ids列表，decode将word-ids转换为相应单词，特殊词句首<S>句尾</S>未知词<UNK>。使用字符词汇表对id和char进行转换，通过查表得到每个词的char_ids表示。词向量与语言模型一起训练，还需要构建word_char_embedding。

单个句子的训练是以[n_token, max_char, char_dim]作为一个训练样本，分别表示句长，单词最大字符长和每个字符维数。我们使用一个大小为[1, n_width, char_dim]的卷积核进行卷积，即高度为1，宽度为n_width，通道数为char_dim的卷积核进行卷积，每次都是一行一行的对n_width大小的字符进行卷积。卷积完之后，我们会形成一个[n_token, max_char-n_width+1]的feature map图，然后我们再对feature map图的每一行进行一个最大池化处理，这样每一个卷积核最终得到[n_token]的数据。我们总共有m=n_filters个卷积核，将每个卷积核的结果拼接起来，最终会形成一个[n_token, m]的数据。

第二个图表示，我们得到了每个词经过m=n_filters个卷积和max pooling形成的feature之后，再通过多层highway网络进行特征筛选处理，最后再通过一个投影层将维度从m投影到p=proj_dim维。highway层和投影层都是可选的。 

```
   http://image.huawei.com/tiny-lts/v1/images/669472629f6c6bb55cd9_1170x536.png@900-0-90-f.png
```

http://image.huawei.com/tiny-lts/v1/images/b6bf72629f6ca0fbfb19_981x458.png@900-0-90-f.png

2.模型结构

```
     2层biLSTM，每层向量维度4096，投影层词向量维度512，最终输入的是128个句子正反向512维的词向量，词向量经过字符卷积得到，每个句子截断为20个词，不足的补齐。

     字符卷积分为一个输入层一个卷积层一个池化层，elmo（16,50），一个词最大长度50，每个字符用16维表示，使用了2048个卷积核，分别是[1, 32], [2, 32], [3, 64], [4, 128], [5, 256], [6, 512], [7, 1024],[宽度，个数]。对每一个行进行最大池化，拼接后形成维度为卷积核个数的词向量，再经过线性变换转为512维。
```

3.源码中训练过程

输入的训练文件应当是分好词的。

Elmo输入后，会以字符单位进行后续的字符卷积，根据词典序号对词进行缩阴，对于字符的索引通过utf-8编码索引。

```
     设置字符向量的维度n后，初始化一个字符总数*n的字符嵌入矩阵，通过索引找到每个词对应字符的向量，进行字符卷积，包括最大池化，经过两个highway layers，进入bilstm。这一层总共有m个词的向量输入，共有m个LSTMCell。

     ELMo最后生成的是上下文相关的词向量，使用的时候输入预训练好的模型，给定任意长度的句子，使用动态rnn，可以算出这个句子每个词的三层向量，有一层是上下文无关的向量（即模型中biLSTM的输入），另外两层是LSTM的输出。

     dump_token_embeddings()保存的是上下文无关词向量，是用词典文件生成的，而dump_bilm_embeddings()是真正的词向量。

     Embeddingsize—与elmo词向量维度一致，hiddenSize—LSTM结构神经元个数，每一个epoch时打乱数据集。
```

4.预训练模型

```
     预训练模型一般分为：语料、编码器、目标任务、微调策略。
```

https://image.jiqizhixin.com/uploads/editor/d12f0728-1f65-4ece-8195-f1c7e2f30347/640.png

具体可见：https://www.jiqizhixin.com/articles/2019-06-25-17

5.优点

上下文相关；单词表示组合了深度预训练神经网络的所有层；基于字符解决了OOV问题--ELMo是按字符单位进行计算，因此处理oov（out of vocab）情况性能比较好

 

参考链接：https://www.cnblogs.com/jiangxinyang/p/10235054.html



