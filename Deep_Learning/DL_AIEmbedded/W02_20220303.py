#Linear Regression
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
tf.enable_eager_execution()

train = pd.read_csv("D:\\vscode\\python\\Deep_Learning\\DL_AIEmbedded\\W02\\train.csv")
train = train[train['LotArea'] < 5000]
train_X = train['LotArea'].values.reshape(-1,1)
train_Y = train['SalePrice'].values.reshape(-1,1)
n_sample = train_X.shape[0]

W = tf.Variable(tf.random_normal([1]))
print(W)
b = tf.Variable(tf.random_normal([1]))
print(b)

for step in range(0,10001):
    with tf.GradientTape() as g:
        pred = W*train_X+b
        loss = tf.reduce_sum(tf.pow(pred-train_Y,2))/n_sample
    gradient = g.gradient(loss,[W,b])
        
    tf.keras.optimizers.Adam(2).apply_gradients(zip(gradient,[W, b]))

    if step % 100 == 0:
        pred= W*train_X+b
        loss = tf.reduce_sum(tf.pow(pred-train_Y,2))/n_sample
        print("step:%i, Loss:%f, W:%f, b:%f "%(step, loss, W.numpy(), b.numpy()))

plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.plot(train_X, np.array(W * train_X + b), label='pred line')
plt.legend()
plt.show()