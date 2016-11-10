统计学习
----
1.the setting and the estimator估计器 object in scikit-learn
<!--了解 数据集和估计器-->
- Datasets数据集
+ A simple example shipped with the scikit: iris dataset(安德森鸢尾花卉数据集:多重变量分析)

+ An example of reshaping data would be the digits dataset： 1797 8x8 images of hand-written digits


— Estimators objects估计器对象
+ Fitting data拟合数据

+ Estimator parameters

+ Estimated parameters


2.监督学习:predicting an output variable from high-dimensional observations 从高维观测值预测输出变量

<!--最近邻算法 线性模型 支持向量机-->
- Nearest neighbor and the curse of dimensionality
    - Classifying irises
    - k-Nearest neighbors classifier
    - Training set and testing set
    - The curse of dimensionality


- Linear线性 model: from regression to sparsity稀疏性
    - Diabetes dataset糖尿病数据集
    - Linear regression线性回归
    - Shrinkage收缩
    - Sparsity稀疏性
    - Classification分类

- Support vector machines (SVMs)

    - Linear SVMs
    
    - Using kernels

3.Model selection:choosing estimators and their parameters
<!--了解 得分估计器, 交叉验证发生器, 栅格搜索  -->
- Score, and cross-validated scores 得分

- Cross-validation generators交叉验证发生器

- Grid-search栅格搜索 and cross-validated estimators


4.Unsupervised learning: seeking representations of the data寻找数据特征
<!--K均值聚类,矢量化, 分层聚集聚类, 信号,组件, 主成分分析, 独立分量分析-->
- K-means clustering K均值聚类
    - Application example: vector quantization矢量量化
    - Hierarchical agglomerative clustering分层聚集聚类: Ward
    
- Decompositions: from a signal to components and loadings 分解：从信号到组件和加载
    - Components and loadings
    - Principal component analysis主成分分析: PCA
    - Independent Component Analysis独立分量分析：ICA

- Putting it all together
    -  Pipelining管道
    -  Face recognition with eigenfaces使用特征面部识别
    -  Open problem: Stock Market Structure开放问题：股票市场结构
