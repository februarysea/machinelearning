# machinelearning

使用Python实现Andrew-Ng老师machine learning课程中的机器学习算法

## week1

```
.
├── algorithm1.py
├── data
│   ├── distances.txt
│   ├── locations.txt
│   ├── prices.txt
│   └── titles.txt
├── data.py
└── figures
    ├── costfunction.png
    └── result.png
```

**单变量线性回归**

步骤：

1. 爬取链家二手房成交数据
2. 处理数据得到二手房与市中心（人民广场）的距离
3. 使用梯度下降法得到线性回归的假设函数

遇到问题：
cost function不收敛：learning rate设置太大，调整后解决

## week2

**多变量线性回归** & **多项式回归**

```
.
├── algorithm2.py
├── algorithm3.py
├── data
│   ├── areas.txt
│   ├── costfunction.txt
│   ├── distances.txt
│   ├── locations.txt
│   ├── names.txt
│   └── prices.txt
├── data.py
└── figures
    ├── multiple.png
    └── polynomial.png
```

步骤：

1. 爬取链家二手房成交数据
2. 处理数据得到二手房与市中心（人民广场）的距离、房屋面积
3. 使用梯度下降法得到线性回归的假设函数

遇到问题：

* 多变量线性回归中cost function收敛过快：将每个features mean normalization后解决
* 多维特征如何可视化没有想到很好的方法

## week3

**logistic回归**

```
.
├── algorithm4.py
├── data
│   └── divorce.csv
└── figures
    └── costfunction.png
```

数据来源：http://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set#

分类问题：通过数据集中的54类特征来预测是否会离婚

将170个样本中，前150个作为训练集，后20个作测试集

添加了accuracy函数来衡量模型的准确度

能明显感觉到特征维度变多后，运行速度下降了不少

遇到问题

```
[1]    93511 segmentation fault  python3 algorithm4.py
```

解决办法是使用虚拟环境
```
python3 -m venv env
```

贴一个原因
https://stackoverflow.com/questions/10035541/what-causes-a-python-segmentation-fault