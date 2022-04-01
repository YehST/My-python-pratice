# coding: utf-8
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from ReferenceData.dataset.mnist import load_mnist
from Basic import SGD
from ReferenceData.common.util import smooth_curve
from ReferenceData.common.multi_layer_net import MultiLayerNet



(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)
x_train = x_train[:300]
t_train = t_train[:300]

optimizer = SGD(lr=0.01)


networks = MultiLayerNet(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100],
                         output_size=10)
max_epochs = 201
train_size = x_train.shape[0]
batch_size = 100
train_loss_list = []
train_acc_list = []
test_acc_list = []

inter_per_epoch = max(train_size/batch_size, 1)
epoch_cnt = 0

for i in range(1000000000):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grads = networks.gradient(x_batch, t_batch)
    optimizer.update(networks.params, grads)

    if i % inter_per_epoch == 0:
        train_acc = networks.accuracy(x_train, t_train)
        test_acc = networks.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        epoch_cnt += 1
        if epoch_cnt >= max_epochs:
            break

x = np.arange(max_epochs)
plt.figure(figsize=(6, 6))
plt.plot(x, train_acc_list, 'r', label='train')
plt.plot(x, test_acc_list, 'b', label='test')
for o in range(0, max_epochs, 10):
    plt.plot(x[o], train_acc_list[o], 'ro')
    plt.plot(x[o], test_acc_list[o], 'bs')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.1)
plt.legend()
plt.show()
