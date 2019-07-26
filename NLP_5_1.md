NLP从入门到不放弃（五）：ELMo（上）
日期：2019-07-10 20:04浏览：20评论：0
一、基础知识

1.RNN循环/递归神经网络

单纯的RNN因为无法处理随着递归，权重指数级爆炸或梯度消失问题，难以捕捉长期时间关联；而结合不同的LSTM可以很好解决这个问题

解决问题：某些任务需要能够更好的处理序列的信息，即前面的输入和后面的输入是有关系的。

https://pic1.zhimg.com/80/v2-206db7ba9d32a80ff56b6cc988a62440_hd.jpg

循环神经网络的隐藏层的值s不仅仅取决于当前这次的输入x，还取决于上一次隐藏层的值s。权重矩阵 W就是隐藏层上一次的值作为这一次的输入的权重。

https://pic2.zhimg.com/80/v2-b0175ebd3419f9a11a3d0d8b00e28675_hd.jpg

 

参考链接：https://zhuanlan.zhihu.com/p/30844905

应用：语言模型和文本生成、机器学习、语音识别、图像描述生成

缺点：需要意识到的是，在vanilla RNNs训练中，BPTT无法解决长时依赖问题(即当前的输出与前面很长的一段序列有关，一般超过十步就无能为力了)，在某些情况下，我们需要更多的上下文信息。考虑一下，我们想要预测下面这句话的最后一个单词“I grew up in France… I speak fluent French.”也就是"French"，根据前面的信息“I speak fluent”我们知道，下一个单词应该是一种语言，但是是哪种语言呢？我们想要确定是哪种语言必须从更前面的语句“I grew up in France“得到更多的信息。因为BPTT会带来所谓的梯度消失或梯度爆炸问题(the vanishing/exploding gradient problem)。当然，有很多方法去解决这个问题，如LSTMs便是专门应对这种问题的。

2.LSTM—长短期记忆网络

https://pic4.zhimg.com/80/v2-2795bc16b012322f7767cd4d940ba2e3_hd.jpg

参考链接：https://zhuanlan.zhihu.com/p/33113729

3.Elmo双向lstm-biLM

â€œelmo åŒå‘lstmâ€çš„å›¾ç‰‡æœç´¢ç»“æžœ

参考前向lstm公式：

可得所需要优化的目标为：



两个网络共同出现的参数说明参数共享，即映射层和上下文矩阵的参数是共享的。

二、训练流程

1.词向量和ELMO向量进行拼接得到最终向量[xk:ELMOtask]；

2.预训练好的模型输入为512维的列向量，LSTM的层数为L=2，每层有4096个单元，每个LSTM输出为512维的列向量，每层LSTM的单元个数为4096个；

3.送入一段话到预训练好的模型，会得到ELMO向量，拼接得到最终向量。

三、其他

1.优势--解决多义词、词性标注、词义消歧（传统词向量通过训练对于每个单词有唯一一个词嵌入表示，不能表示多义词，ELMo的做法是预训练语言模型，词嵌入是根据输入的句子实时输出，单词的意义是上下文相关的）

2.缺点

LSTM作为特征抽取器，提取特征能力不如Transformer 

采取双向拼接作为融合特征的能力可能不如bert一体化的融合特征方式

3.参考链接

https://allennlp.org/elmo

```
              https://zhuanlan.zhihu.com/p/51679783
```

四、基于中文的ELMo训练

```
   1.各种版本

             基于pytorch的ALLenNLP：https://github.com/allenai/allennlp

             基于tensorflow：https://github.com/allenai/bilm-tf

             hit用pytorch重写的有各种训练好的模型：https://github.com/HIT-SCIR/ELMoForManyLangs

            一个哭唧唧的小提示：allenNLP要求torch版本0.4.0，各位选手请注意自己的服务器是gpu还是cpu。默认服务器搭载了gpu真的是对自己的身份有了非常大的误解

            另一个暴风哭泣的小提示：官网搜索的版本，如果是附了个链接pip下载的，建议下载到本地传到服务器再安装（强颜欢笑.jpg
```

```
   2.hit版参数设置

             python -m elmoformanylangs.biLM train \
             --train_path home/50002577/Elmo/wiki_small_seg.txt \ #训练的数据，需要提前分词一句一行
             --config_path home/50002577/Elmo/configs/cnn_50_100_512_4096_sample.json \ #配置文件 .json
             --model home/50002577/Elmo/testmodel\ #输出路径
             --optimizer adam \
             --lr 0.001 \

             --lr_decay 0.8 \ 
             --max_epoch 1 \ #迭代次数

             --max_sent_len 30 \ #处理的滑窗长度
             --max_vocab_size 150000 \ 
             --min_count 3 #最少word数量

             python -m elmoformanylangs test \
             --input_format conll \ #输入格式
             --input /path/to/your/input \
             --model /path/to/your/model \
             --output_prefix /path/to/your/output \
             --output_format hdf5 \
             --output_layer -1 #0-cnn encoded word 1-第一层lstm 2-第二次lstm   

             更多参数可以在biLM.py文件里找到

       参考链接：https://blog.csdn.net/jeryjeryjery/article/details/80839291

                     https://www.cnblogs.com/jiangxinyang/p/10235054.html

                     https://blog.csdn.net/firesolider/article/details/88092831
```

​                         
​                         
   NLP从入门到不放弃（六）：bert及一些对比
日期：2019-07-15 20:46浏览：10评论：0
·FastText与Word2Vec对比

```
     FastText速度更快，专注于文本分类，在文本倾向性分析或标签预测方面都有非常好的表现，但是输出层是对应分类的标签而不是词向量。Word2Vec输入层是滑窗里的文本，而Fasttext输入层是包括滑窗文本和N-gram的内容，可以进行无监督学习，也可以进行有监督学习，学习目标是人工标注分类结果。
```

Fasttext目前已有训练好的维基词向量https://fasttext.cc/docs/en/pretrained-vectors.html

·glove与LSA对比

```
     LSA是基于共现矩阵构建词向量，实质上是基于全局语料采用SVD进行矩阵分解，计算复杂度高，gloVe可以看做对LSA一种优化算法，性能远超LSA。
```

·Elmo与word2vec

```
     Elmo的词向量是上下文相关的，而w2v是固定的
```

·glove与word2vec

```
     W2v特征提取基于滑窗，而glove是基于全局语料的，滑窗是为了构建共现矩阵，因此word2vec可以进行增量学习在线学习，glove需要固定语料。

     W2v是无监督学习，glove需要label-共现次数。
```

·基于计数和基于预测两种词嵌入方式

```
     基于计数优点：
```

1. 训练非常迅速。
2. 能够有效的利用统计信息。

缺点：

1. 主要用于获取词汇之间的相似性（其他任务表现差）
2. 给定大量数据集，重要性与权重不成比例。

基于预测的方法的优点：

1. 能够对其他任务有普遍的提高。
2. 能够捕捉到含词汇相似性外的复杂模式。

缺点：

1. 需要大量的数据集。
2. 不能够充分利用统计信息。

·elmo、gpt、bert

```
     Elme采用LSTM进行特征提取，GPT和bert采用transformer进行提取。
```

gpt采用单向语言模型；elmo采用两个方向相反的单项语言模型拼接，与bert将上下文用一套模型参数进行编码不同，使用的是两个分开的单向rnn去处理，只是共享输入和输出时拼接，不需要mask；bert双向语言模型-实际使用Masked LM实现双向encoding。

gpt采用decoder部分，bert采用encoder。

·bert

```
     捕捉token级特征核心思想：Masked LM，transformer encoder

     Masked LM：将整个句子的词随机选择去盖住，用模型预测盖住的词。对于一个被盖住的词：

               ·有80%概率用[mask]标记替换
```

·有10%概率用随机采样的一个单词替换

·有10%概率不做替换

```
     Transformer encoder：可以无视方向和距离将句子中每个词encoding进来，自带了全局的self-attention，且比LSTM更容易无视mask标记的影响。位置信息采用粗暴的位置标记法。

     最终叠加了24层multi-head attention block，每个block包含16抽头和1024隐单元作为encoder。

     捕捉句子级特征核心思想：负采样

     类似word2vec构造句子级别的分类任务。对应一个给定的句子（相当于word2vec中给定context），它下一个句子即为正例（相当于word2vec中的正确词），随机采样一个句子作为负例（相当于word2vec中随机采样的词），然后在该sentence-level上来做二分类（即判断句子是当前句子的下一句还是噪声）。通过这个简单的句子级负采样任务，BERT就可以像word2vec学习词表示那样轻松学到句子表示。
```

一些其他的：

```
     Elmo如果使用自己的语料包进行训练，建议cpu选手就此止步。普通选手在Elmo和bert都建议使用预训练模型进行下游任务。

     微软五月份提出了一个新的通用预训练模型MASS，专注于seg2seg的自然语言生成任务，需要可以查看如下链接：
```

https://xw.qq.com/partner/hwbrowser/20190510A07W00/20190510A07W0000?ADTAG=hwb&pgv_ref=hwb&appid=hwbrowser&ctype=news

 

参考链接：https://www.jiqizhixin.com/articles/2018-12-24-19

```
                  https://zhuanlan.zhihu.com/p/50946044
```

​                      
