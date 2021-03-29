from matplotlib import pyplot as plt 
import numpy as np

def gradient_descent(x:list, y:list):
    cost_functions = []

    # the number of training set
    m = len(x)

    # learning rate alpha
    alpha = 0.0001

    # parameteres
    # theta0, theta1
    theta0 = 300
    theta1 = 1
    
    # gredient descent loop
    k = 1
    while k< 200001:
        total = 0
        for i in range(0, m):
            total = total + pow((theta0 + theta1 * x[i] - y[i]), 2)
        cost_function = total / (2 * m)
        cost_functions.append(cost_function)
        print(f"time:{k},cost:{cost_function}")

        total_theta0 = 0
        for i in range(0, m):
            total_theta0 = total_theta0 + (theta0 + theta1 * x[i] - y[i]) 

        total_theta1 = 0
        for i in range(0, m):
            total_theta1 = total_theta1 + ((theta0 + theta1 * x[i] - y[i]) * x[i])

        temp0 = theta0 - alpha * total_theta0 / m
        temp1 = theta1 - alpha * total_theta1 / m
        theta0 = temp0
        theta1 = temp1

        k = k + 1
    plot_figure(x=x, y=y, theta0=theta0, theta1=theta1)
    return cost_functions


def plot_figure(x, y, theta0, theta1):
    distances = [x for x in range(0,40)]
    prices = [theta0+theta1*distance for distance in distances]

    x = np.array(x)
    y = np.array(y)
    plt.title("second-hand house price and distance from downtown")
    plt.xlabel("distance(KM)")
    plt.ylabel("price(W)")
    plt.plot(x,y, 'ro')
    plt.plot(distances,prices)
    plt.show()


if __name__ == "__main__":
    with open("data/distances.txt", 'r') as f:
        distances = f.read().split("\n")
    with open("data/prices.txt", 'r') as f:
        prices = f.read().split("\n")
    for i in range(0, len(distances)):
        distances[i] = float(distances[i])
    for i in range(0, len(prices)):
        prices[i] = float(prices[i])
    
    x = np.arange(1,200001)
    y = np.array(gradient_descent(x=distances, y=prices))
    plt.title("Gradient Descent") 
    plt.xlabel("times") 
    plt.ylabel("cost function") 
    plt.plot(x, y) 
    plt.show()
