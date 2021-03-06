import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
print(tf.__version__)

num_class = 10
batch_size = 2048
epochs = 30
iteration = 30
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train, x_test = x_train.astype('float32'), x_test.astype('float32')
x_train = np.reshape(
    x_train, (x_train.shape[0], x_train.shape[1], x_train.shape[2], 1))
x_test = np.reshape(
    x_test, (x_test.shape[0], x_test.shape[1], x_test.shape[2], 1))
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)


def conv(x, filters, size):
    return tf.keras.layers.Conv2D(filters=filters, kernel_size=size)(x)


def maxpooling(x):
    return tf.keras.layers.MaxPooling2D(padding='same', strides=2)(x)


def Lenet(x):
    x = conv(x, 6, (5, 5))
    x = maxpooling(x)
    x = conv(x, 16, (5, 5))
    x = maxpooling(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dropout(rate=0.2)(x)
    x = tf.keras.layers.Dense(120, activation='tanh')(x)
    x = tf.keras.layers.Dropout(rate=0.2)(x)
    x = tf.keras.layers.Dense(84, activation='tanh')(x)
    x = tf.keras.layers.Dropout(rate=0.2)(x)
    x = tf.keras.layers.Dense(10, activation='softmax')(x)
    return x


img_input = tf.keras.Input(shape=(28, 28, 1))
output = Lenet(img_input)
model = tf.keras.Model(img_input, output)
print(model.summary())

opt = tf.keras.optimizers.Adam(0.0035)
model.compile(optimizer=opt,
              loss='categorical_crossentropy', metrics=['acc'])
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_acc', factor=0.8, patience=1, min_lr=0.0001)
history = model.fit(x=x_train, y=y_train, batch_size=batch_size, epochs=epochs,
                    steps_per_epoch=iteration, validation_data=(x_test, y_test), callbacks=[reduce_lr])

model.save('./mnist_Lenet.h5')

plt.figure(figsize=(18, 6))
plt.subplot(131)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='lower right')
plt.subplot(132)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.subplot(133)
plt.plot(history.history['lr'])
plt.title('Model lr')
plt.ylabel('lr')
plt.xlabel('Epoch')
plt.show()
