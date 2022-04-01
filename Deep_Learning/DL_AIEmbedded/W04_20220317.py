import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
import tensorflow as tf
from W04_Model import model_Adam, model_SGD, model_AdaGrad, model_Adadelta

'''_______data catch_______'''
iris = datasets.load_iris()
X = iris.data
Y = iris.target
dataset = []
for index, x in enumerate(X):
    x = [x[0], x[1], x[2], x[3]]
    dataset.append((x))
dataset = np.array(dataset)

X_train, X_test, Y_train, Y_test = train_test_split(dataset, Y, test_size=0.3, random_state=0)
Y_train = tf.keras.utils.to_categorical(Y_train, 3)
Y_test = tf.keras.utils.to_categorical(Y_test, 3)
#print(model1.summary())
'''_______model compile & training_______'''

history1 = model_SGD(X_train, Y_train, X_test, Y_test)
history2 = model_Adam(X_train, Y_train, X_test, Y_test)
history3 = model_AdaGrad(X_train, Y_train, X_test, Y_test)
history4 = model_Adadelta(X_train, Y_train, X_test, Y_test)
history = {'SGD':history1,'Adam':history2, 'Adagrad':history3, 'Adadelta':history4 }

for opt in history.keys():
    plt.figure(opt,figsize=(12, 4))
    plt.subplot(131)
    plt.plot(history[opt].history['acc'])
    plt.plot(history[opt].history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc = 'lower right')
    plt.subplot(132)
    plt.plot(history[opt].history['loss'])
    plt.plot(history[opt].history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc = 'upper right')
    plt.subplot(133)
    plt.plot(history[opt].history['lr'])
    plt.title('Model lr')
    plt.ylabel('Lr')
    plt.xlabel('Epoch')
    plt.legend(['lr'], loc = 'upper right')
plt.show()