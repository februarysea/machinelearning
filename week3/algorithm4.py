# algorithm4.py
# logistic regression

import numpy as np
from matplotlib import pyplot as plt

def logistic_regression(x, y):
    cost_functions = []

    # the number of sample
    m = len(x)
    # the number of fearture
    n = len(x[0])
    # learning rate
    alpha = 0.001
    # initialization theta
    theta = np.zeros([n, 1])

    k = 1
    while k<5001:
        # caculate cost function
        cost_total = 0
        for i in range(0, m):
            thetaT_multiply_x = np.matmul(theta.T, x[i])
            h_x = 1 / (1 + np.exp(-thetaT_multiply_x))
            cost_total = cost_total + y[i] * np.log(h_x) + (1-y[i]) * np.log(1-h_x)
        cost_function = - cost_total / m
        cost_functions.append(cost_function)

        # gradient descent
        temp_theta = np.empty([n, 1])
        descent_total = 0
        for j in range(0, n):
            for i in range(0, m):
                thetaT_multiply_x = np.matmul(theta.T, x[i])
                h_x = 1 / (1 + np.exp(-thetaT_multiply_x))
                descent_total = descent_total + (h_x - y[i]) * x[i][j]
            temp_theta[j] = theta[j] - alpha / m * descent_total
        theta = temp_theta
        print(f"time:{k}, cost function:{cost_function[0]}")
        k = k + 1

    plot_figure(cost_functions)
    return theta

def test_model(theta, x, y):
    # 1 means right
    # 0 means wrong
    accuracy =[]
    m = len(x)
    for i in range(0, m):
        thetaT_multiply_x = np.matmul(theta.T, x[i])
        h_x = 1 / (1 + np.exp(-thetaT_multiply_x))
        if h_x>=0.5:
            if y[i]==1:
                accuracy.append(1)
            else:
                accuracy.append(0)
        else:
            if y[i]==0:
                accuracy.append(1)
            else:
                accuracy.append(0)
    print(f"accuracy:{round(accuracy.count(1) / len(accuracy), 2)}")

def plot_figure(cost_functions):
    x = np.arange(1, len(cost_functions)+1)
    y = np.array(cost_functions)
    plt.title("cost function tendency")
    plt.xlabel("times") 
    plt.ylabel("cost function")
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    with open("data/divorce.csv", 'r') as f:
        data = f.read()
        data = data.split("\n")
    for i in range(0,len(data)):
        data[i] = data[i].split(';')
        for k in range(0, len(data[i])):
            data[i][k] = int(data[i][k])
        # add x0 = 1
        data[i] = [0] + data[i]
    
    data = np.array(data)
    
    m = len(data)
    n = len(data[0])
    x = np.empty(shape=[m, n-1], dtype=int)
    y = np.empty(shape=[m, 1], dtype=int)
    for i in range(0,m):
        x[i] = data[i][0:-1]
        y[i] = data[i][-1]
    
    # training set and test set
    training_x = x[0:len(data)-20]
    training_y = y[0:len(data)-20]
    test_x = x[len(data)-20:]
    test_y = y[len(data)-20:]

    theta = logistic_regression(x=training_x, y=training_y)
    test_model(theta=theta, x=test_x, y=test_y)