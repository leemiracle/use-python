布尔检索
----
1.信息检索按照数据的规模分成 3 个主要级别
    -  Web 搜索(web search)为代表的大规模级别,此时需要处理存储在数百万台计算机上的数十亿篇文档.问题包括:如何采集到这种规模的文档?如何在这种大规模数据量的情况下建立高效运行的系统?如何应对Web 特性所带来的特殊问题(比如,怎样利用超链接信息,如何防止一些别有用心的人通过伪
造网页内容来提高其网站在商业搜索引擎中的排名,等等)?
    -  第二个级别是小规模,如个人信息检索
    -  中等规模的数据,包括面向企业、机构和特定领域的搜索(domain-specific search),比如对公司内部文档、专利库或生物医学文献的搜索。文档往往存储在集中的文件系统中,由一台或者多台计算机提供搜索服务。

2.线性扫描方式，如grep

3.非线性扫描
    - 事先给文档建立索引(index),
    - 词项,假定我们对每篇文档(这里指每部剧本)都事先记录它是否包含词表中的某个词,结果就会得到一个由布尔值构成的词项—文档关联矩阵(incidence matrix)。词项(term)是索引的单位.
    - 根据从行还是列的角度来看,可以得到不同的向量
    - “ 文档” (document)指的是检索系统的检索对象,它们可以是一条条单独的记录或者是一本书的各章
    - 所有的文档组成文档集(collection),有时也称为语料库(corpus)
    - ad hoc检索(ad hoc retrieval)任务
    - 正确率(Precision): 返回的结果中真正和信息需求相关的文档所占的百分比。
    - 召回率(Recall): 所有和信息需求真正相关的文档中被检索系统返回的百分比。
    - 出现某词项的文档的数目,即文档频率(document frequency)
    - 查询优化(query optimization)指的是如何通过组织查询的处理过程来使处理工作量最小。
    - 倒排索引(inverted index): 因为一般提到的索引都是从词项反向映射到文档的。左部称为词项词典(dictionary,简称词典,有时也称为vocabulary或者lexicon。), 这个表中的每个元素通常称为
倒排记录(posting)。每个词项对应的整个表称为倒排记录表(posting list)或倒排表(inverted list)。所有词项的倒排记录表一起构成全体倒排记录表(postings)。倒排记录表则按照文档ID号进行排序。
    
4.构建倒排索引
    - (1) 收集需要建立索引的文档
    - (2) 将 每 篇 文 档 转 换 成 一 个 个 词 条( token ) 的 列 表 , 这 个 过 程 通 常 称 为 词 条 化(tokenization)
    - (3) 进行语言学预处理,产生归一化的词条来作为词项
    - (4). 对所有文档按照其中出现的词项来建立倒排索引,索引中包括一部词典和一个全体倒排记录表。
    - (5)建立索引最核心的步骤是将这个列表按照词项的字母顺序进行排序,倒排记录表会按照docID进行排序
    - (6)对于内存中的一个倒排记录表,可以采用两种好的存储方法:一个是单链表,另一个是变长数组。单链表(singly linked list)便于文档的插入和
更新(比如,对更新的网页进行重新采集),因此通过增加指针的方式可以很自然地扩展到更高级的索引策略,变长数组(variable length array)的存储方式一方面可以节省指针消耗的空间,另一方面由于采用连续的内存存储,可以充分利用现代计
算机的缓存(cache)技术来提高访问速度。额外的指针在实际中可以编码成偏移地址融入到表中。如果索引更新不是很频繁的话,变长数组的存储方式在空间上更紧凑,遍历也更快。

4.布尔查询的处理
    - (1) 在词典中定位 Brutus;
    - (2) 返回其倒排记录表;
    - (3) 在词典中定位 Calpurnia;
    - (4) 返回其倒排记录表;
    - (5) 对两个倒排记录表求交集
    - (6) 查询优化：不是将倒排记录表合并看成两个输入加一个不同输出的函数,而是将每个返回的倒排记录表和当前内存中的中间结果进行合并,这样做的效率更高而最初的中间结果中可以调入最小文档频率的词项所对应的倒排记录表。
该合并算法是不对称的:中间结果表在内存中而需要与之合并的倒排记录表往往要从磁盘中读取。

5.对基本布尔操作的扩展及有序检索
    - 邻近操作符(proximity)用于指定查询中的两个词项应该在文档中互相靠近,靠近程度通常采用两者之间的词的个数或者是否同在某个结构单元(如句子或段落)中出现来衡量。
    
