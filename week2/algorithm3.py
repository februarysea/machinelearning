# polynomial regression
# multiple varaiables

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# parameteres
# theta0, theta1,theta2
theta0 = 300
theta1 = 1
theta2 = 0.1
theta3 = 0.01

def gradient_descent(x:list, y:list):
    cost_functions = []
    x1 = x
    x2 = []
    x3 = []
    # the number of training set
    m = len(y)

    # learning rate alpha
    alpha = 0.0004

    # caculate
    for i in range(0, m):
        x2.append(x[i] * x[i])
        x3.append(x[i] * x[i] * x[i])

    global theta0
    global theta1 
    global theta2
    global theta3
    
    # gredient descent loop
    k = 1
    while k< 100001:
        total = 0
        for i in range(0, m):
            total = total + pow((theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]), 2)
        cost_function = total / (2 * m)
        cost_functions.append(cost_function)
        print(f"time:{k},cost:{cost_function}")

        total_theta0 = 0
        for i in range(0, m):
            total_theta0 = total_theta0 + (theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i])

        total_theta1 = 0
        for i in range(0, m):
            total_theta1 = total_theta1 + (theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) *x1[i]

        total_theta2 = 0
        for i in range(0, m):
            total_theta2 = total_theta2 + (theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) * x2[i]
        
        total_theta3 = 0
        for i in range(0, m):
            total_theta3 = total_theta3 + (theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) * x3[i]

        temp0 = theta0 - alpha * total_theta0 / m
        temp1 = theta1 - alpha * total_theta1 / m
        temp2 = theta2 - alpha * total_theta2 / m
        temp3 = theta3 - alpha * total_theta3 / m
        theta0 = temp0
        theta1 = temp1
        theta2 = temp2
        theta3 = temp3

        k = k + 1
    return cost_functions

def plot_cost_function(cost_functions:list):
    x = np.arange(1,100001)
    y = np.array(cost_functions)
    plt.title("Gradient Descent") 
    plt.xlabel("times") 
    plt.ylabel("cost function") 
    plt.plot(x, y) 
    plt.show()

def plot_figure(x:list, y:list):
    # TODO
    pass

if __name__ == "__main__":
    with open("data/distances.txt", 'r') as f:
        distances = f.read().split("\n")
    with open("data/prices.txt", 'r') as f:
        prices = f.read().split("\n")
    
    m = len(prices)

    for i in range(0, m):
        distances[i] = float(distances[i])
    for i in range(0, m):
        prices[i] = float(prices[i])

    # mean normalization
    temp = []
    for i in range(0, m):
        mean = sum(distances) / m
        temp.append(round((distances[i] - mean) / (max(distances) - min(distances)), 2))
    normolization_distances = temp
    # result
    cost_function = gradient_descent(x=normolization_distances, y=prices)
    plot_cost_function(cost_function)
    plot_figure(x1=distances, y=prices)
   