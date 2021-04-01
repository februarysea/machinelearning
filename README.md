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