1.Classification分类

- Identifying to which category an object belongs to.识别对象属于哪个分类
- Applications: Spam detection垃圾邮箱检测, Image recognition图像识别.
- Algorithms: 
    - SVM支持向量机(特征空间上的间隔最大的线性分类器，其学习策略便是间隔最大化，最终可转化为一个凸二次规划问题的求解。), 
    - nearest neighbors最近邻(k-Nearest Neighbor，KNN)分类算法.如果一个样本在特征空间中的k个最相 似(即特征空间中最邻近)的样本中的大多数属于某一个类别，则该样本也属于这个类别。
    - random forest随机森林(通过训练多个决策树，生成模型，然后综合利用多个决策树进行分类。), ...

2.Regression回归

- Predicting a continuous-valued attribute associated with an object.预测对象的一个 连续性的属性值
- Applications: Drug response药物反应, Stock prices股票价格.
- Algorithms: 
    - SVR支持向量回归机, 
    - ridge regression岭回归(是在平方误差的基础上增加正则项), 
    - Lasso又译最小绝对值收敛和选择算子、套索算法

3.Clustering聚类

- Automatic grouping of similar objects into sets.将类似对象自动分组
- Applications: Customer segmentation客户细分, Grouping experiment outcomes分组实验结果
- Algorithms: 
    - k-Means将样本聚类成k个簇,  随机选取k个聚类质心点（cluster centroids）. 重复下面过程直到收敛 {对于每一个样例i，计算其应该属于的类, 对于每一个类j，重新计算该类的质心}
    - spectral clustering谱聚类,将带权无向图划分为两个或两个以上的最优子图，使子图内部尽量相似，而子图间距离尽量距离较远，以达到常见的聚类的目的。其中的最优是指最优目标函数不同，可以是割边最小分割
    - mean-shift先算出当前点的偏移均值,移动该点到其偏移均值,然后以此为新的起始点,继续移动,直到满足一定的条件结束.

4.Dimensionality reduction降维

- Reducing the number of random variables to consider.减少要考虑的随机变量的数量
- Applications: Visualization可视化, Increased efficiency增加效率
- Algorithms: 
    - PCA主成分分析算法, 用一种较少数量的特征对样本进行描述以达到降低特征空间维数的方法，它的本质实际上是K-L变换
    - feature selection特征选取, 目标是选择那些在某一特定评价标准下的最重要的特征子集
    - non-negative matrix factorization非负矩阵分解.

5.Model selection模型选择

- Comparing, validating and choosing parameters and models.比较,评估、选择参数和模型
- Goal: Improved accuracy via parameter tuning 通过参数调整提高精度
- Modules: grid search网格搜索, cross validation交叉验证, metrics指标.

6.Preprocessing预处理

- Feature extraction and normalization.特征提取和归一化
- Application: Transforming input data such as text for use with machine learning algorithms.转换输入数据如文本,以供机器学习算法使用
- Modules: preprocessing, feature extraction.
