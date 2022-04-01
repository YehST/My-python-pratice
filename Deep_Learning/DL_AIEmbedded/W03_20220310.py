#Logistic Regression
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target
dataset = []
target_label = 0
for index, x in enumerate(X):
    tranform_label = None
    if Y[index] == target_label:
        tranform_label = 1
    else:
        tranform_label = 0
    x = [x[0],x[2]]
    dataset.append((x,tranform_label))
dataset = np.array(dataset)

def sigmoid(z):
    return 1/(1+np.exp(-z))

def gradient(dataset, w):
    index = random.randint(0, len(dataset) - 1)
    x, y = dataset[index]
    x = np.array(x)
    error = sigmoid(w.T.dot(x))
    g = (error - y) * x
    return g   

def cost(dataset, w):
    total_cost = 0
    for x, y in dataset:
        x = np.array(x)
        error = sigmoid(w.T.dot(x))
        total_cost += abs(y - error)
    return total_cost

def logistic_regression(dataset):
    w = np.zeros(2)
    limit = 1500
    eta = 0.12
    costs = []
    for i in range(limit):
        current_cost = cost(dataset, w)
        if i % 100 == 0:
            print("epoch = "+str(i/100+1)+" : current_cost = " , current_cost , " : w = ",w)
        costs.append(current_cost)
        w = w - eta * gradient(dataset, w)
        eta *= 0.9999
    plt.plot(range(limit), costs)
    plt.show()
    return w,(limit, costs)

def main():
    w = logistic_regression(dataset)
    # draw
    ps = [v[0] for v in dataset]
    label = [v[1] for v in dataset]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #plot via label
    tpx = []
    for index, label_value in enumerate(label):
        px = ps[index][0]
        py = ps[index][1]
        tpx.append(px)
        if label_value == 1:
            ax1.scatter(px, py, c = 'b', marker='o')
        else:
            ax1.scatter(px, py, c = 'r', marker='x')

    l = np.linspace(min(tpx),max(tpx))
    a, b = (-w[0][0]/w[0][1],w[0][0])
    ax1.plot(l, a*l, 'g-')
    plt.show()

if __name__ == '__main__':
    main()
