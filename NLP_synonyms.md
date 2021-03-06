NLP从入门到不放弃之同义词服务——synonyms
日期：2019-07-20 11:49浏览：8评论：0
一、synonyms源码阅读

1.Seg：分词

2.nearby：输入一个word，通过9转换为utf-8编码，通过word2vec的neighbours()函数找到前十个相近的词—使用kdtree，按(词，分数)输出

-----neighbours()：移除头尾的空格、换行符，得到词向量，在kd树上查找，

3.compare：比较句子相似度，对于未登录词，可以忽视或随机选择向量，去停用词，使用_similartity_distance()返回相似度

----_similartity_distance()对向量计算余弦距离，后平滑

4.display：显示近义词，使用nearby找到近义词，遍历输出k-v对即

5.KeyedVectors：

6.sigmoid：sigmoid函数

7.cosine：计算余弦距离

8.any2unicode：将string转换为utf-8编码

github链接：https://github.com/huyingxi/Synonyms/blob/master/synonyms/word2vec.py

二、邻近搜索

方案一：暴力搜索

对于D维空间上N个样本，计算复杂度为O(DN2)，sklearn.neighbours中设定参数algorithm=‘brute’指定暴力搜索，在N过大时不可用。

方案二：KDTree（转载）

为了解决二维节点比较大小，在平面上选点划分，形成的树

```
     黄色的点作为根节点，上面的点归左子树，下面的点归右子树，接下来再不断地划分，最后得到一棵树就是赫赫有名的BSPTree（binary space partitioning tree）. 分割的那条线叫做分割超平面（splitting hyperplane），在一维中是一个点，二维中是线，三维的是面。
```

KDTree就是超平面都垂直于轴的BSPTree。同样的数据集，用KDTree划分之后就是这样：

https://img-blog.csdn.net/20141125170640843     https://img-blog.csdn.net/20141126094947004

1.树的建立

```
     先定义一下节点的数据结构。每个节点应当有下面几个域：

     Node-data -  数据矢量， 数据集中某个数据点，是n维矢量（这里也就是k维）
```

Range  - 空间矢量， 该节点所代表的空间范围

split  - 整数， 垂直于分割超平面的方向轴序号

Left  - k-d树， 由位于该节点分割超平面左子空间内所有数据点所构成的k-d树

Right  - k-d树， 由位于该节点分割超平面右子空间内所有数据点所构成的k-d树

parent  - k-d树， 父节点

建立树最大的问题在于轴点（pivot）的选择，选择好轴点之后，树的建立就和BSTree差不多了。

建树必须遵循两个准则：

1.建立的树应当尽量平衡，树越平衡代表着分割得越平均，搜索的时间也就是越少。

2.最大化邻域搜索的剪枝机会。

2.最近邻域搜索

给定一个KDTree和一个节点，求KDTree中离这个节点最近的节点.(这个节点就是最临近点)。这里距离的求法用的是欧式距离。

https://img-blog.csdn.net/20141126160122781

基本的思路很简单：首先通过二叉树搜索（比较待查询节点和分裂节点的分裂维的值，小于等于就进入左子树分支，等于就进入右子树分支直到叶子结点），顺着“搜索路径”很快能找到最近邻的近似点，也就是与待查询点处于同一个子空间的叶子结点；然后再回溯搜索路径，并判断搜索路径上的结点的其他子结点空间中是否可能有距离查询点更近的数据点，如果有可能，则需要跳到其他子结点空间中去搜索（将其他子结点加入到搜索路径）。重复这个过程直到搜索路径为空。

下面再用一个例子来具体说一下查询的过程。

假设我们的k-d tree就是上面通过样本集{(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)}创建的。

我们来查找点(2.1,3.1)，在(7,2)点测试到达(5,4)，在(5,4)点测试到达(2,3)，然后search_path中的结点为<(7,2), (5,4), (2,3)>，从search_path中取出(2,3)作为当前最佳结点nearest, dist为0.141；

然后回溯至(5,4)，以(2.1,3.1)为圆心，以dist=0.141为半径画一个圆，并不和超平面y=4相交，如下图，所以不必跳到结点(5,4)的右子空间去搜索，因为右子空间中不可能有更近样本点了。

于是在回溯至(7,2)，同理，以(2.1,3.1)为圆心，以dist=0.141为半径画一个圆并不和超平面x=7相交，所以也不用跳到结点(7,2)的右子空间去搜索。

至此，search_path为空，结束整个搜索，返回nearest(2,3)作为(2.1,3.1)的最近邻点，最近距离为0.141。

再举一个稍微复杂的例子，我们来查找点(2,4.5)，在(7,2)处测试到达(5,4)，在(5,4)处测试到达(4,7)，然后search_path中的结点为<(7,2), (5,4), (4,7)>，从search_path中取出(4,7)作为当前最佳结点nearest, dist为3.202；

然后回溯至(5,4)，以(2,4.5)为圆心，以dist=3.202为半径画一个圆与超平面y=4相交，如下图，所以需要跳到(5,4)的左子空间去搜索。所以要将(2,3)加入到search_path中，现在search_path中的结点为<(7,2), (2, 3)>；另外，(5,4)与(2,4.5)的距离为3.04 < dist = 3.202，所以将(5,4)赋给nearest，并且dist=3.04。

回溯至(2,3)，(2,3)是叶子节点，直接平判断(2,3)是否离(2,4.5)更近，计算得到距离为1.5，所以nearest更新为(2,3)，dist更新为(1.5)

回溯至(7,2)，同理，以(2,4.5)为圆心，以dist=1.5为半径画一个圆并不和超平面x=7相交, 所以不用跳到结点(7,2)的右子空间去搜索。

至此，search_path为空，结束整个搜索，返回nearest(2,3)作为(2,4.5)的最近邻点，最近距离为1.5。

构建KD树速度较快，当低维即D较低时，查询近邻速度为O(logN)，但只对低维搜索速度快，当D变大时查询速度为O(DN)效率不高。可以通过设置参数 algorithm=’kd_tree’设置。

参考链接：https://blog.csdn.net/silangquan/article/details/41483689

方案三：Ball Tree（转载）

为了解决 KD 树在高维上效率低下的问题, ball 树 数据结构就被研发出来了. 其中 KD 树沿卡迪尔轴（即坐标轴）分割数据, ball 树在沿着一系列的 hyper-spheres 来分割数据。通过这种方法构建的树要比 KD 树消耗更多的时间，但是这种数据结构对于高结构化的数据是非常有效的, 即使在高维度上也是一样。

ball 树将数据递归地划分为由质心 C和半径r定义的节点,使得节点中的每个点位于由r和C定义的 hyper-sphere 内. 通过使用 triangle inequality（三角不等式） 减少近邻搜索的候选点数:|x+y|<=|x|+|y|通过这种设置, 测试点和质心之间的单一距离计算足以确定距节点内所有点的距离的下限和上限. 由于 ball 树节点的球形几何, 它在高维度上的性能超出 KD-tree, 尽管实际的性能高度依赖于训练数据的结构。

搜索时间大致随O(DlogN)增长，可以通过设置参数algorithm=’ball_tree’指定。

参考链接：https://www.zhihu.com/question/30957691/answer/338362344
方案四：annoy（转载）

点击链接查看原理：https://blog.csdn.net/hero_fantao/article/details/70245387

问题：这是一个精确度换速度的算法，找到的k紧邻不能保证是全局的k紧邻（例如在分割平面附近的点），所以如果要找exact的k紧邻的话并不合适，还是得做全局的搜索。可以通过设置tree的数量来balance精度和速度。每次对同一份数据建立索引是不同的，所以两次计算结果可能也会不同。

源码链接：https://github.com/spotify/annoy

