from ReferenceData.dataset.mnist import load_mnist
from Basic import Act_Func
import sys
import os
import pickle
import numpy as np
from PIL import Image
sys.path.append(os.pardir)


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(
        flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open(r"D:\vscode\python\Deep_Learning\DL_From_scrach\ch03\sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = Act_Func.sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = Act_Func.sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = Act_Func.softmax(a3)  # y為x = 0~9 中每個數字的機率陣列

    return y


x, t = get_data()
network = init_network()

batch_size = 100  # 批次數量
accuracy_cnt = 0
for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])
    #y = predict(network, x[i])
    # p = np.argmax(y)  # 取出最大值之索引值擔任預測結果
    # if p == t[i]:
    #    accuracy_cnt += 1
# print(y)
print("Accuacy:"+str(float(accuracy_cnt/len(x))))
