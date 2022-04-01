#模型量化 --> Ubuntu優化 --> 板端執行
import tensorflow as tf
import numpy as np
import glob

IMAGE_SIZE = 28

def color_preprocessing(x_train, x_test):
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train = x_train/ 255.
    x_test = x_test /255.
    return x_train, x_test

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)
x_train, x_test = color_preprocessing(x_train, x_test)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], x_train.shape[2], 1))

def representative_data_gen():

    dataset_list_index = np.random.choice(range(50000), 100)
    for i in range(100):
        image = x_train[dataset_list_index[i]]
        image = tf.image.resize(image, [IMAGE_SIZE, IMAGE_SIZE])
        image = tf.cast(image, tf.float32)
        image = tf.expand_dims(image, 0)
        with tf.Session() as sess:
            image = sess.run(image)
        yield [image]

converter = tf.lite.TFLiteConverter.from_keras_model_file(r'D:\vscode\python\Deep_Learning\DL_AIEmbedded\Model\MNIST_LeNet\SGD\lr005_30e\mnist_Lenet.h5')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops= [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8
converter.representative_dataset = representative_data_gen
tflite_model = converter.convert()

with open('mnist115.tflite', 'wb') as f:
    f.write(tflite_model)
