import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#版本需相同
model = tf.keras.models.load_model(r'D:\vscode\python\Deep_Learning\DL_AIEmbedded\Model\MNIST_LeNet\Adam\lr0015_Dropout_PerformanceScheduling_30e\mnist_Lenet.h5')



plt.figure(figsize=(6, 4))
y = 0
for i in range(10):
    img = Image.open(f'.\\python\\Deep_Learning\\DL_AIEmbedded\\number_data\\number_PNG2/{i}.png')
    y += 1
    x = int('32'+str(y))
    if y >= 7:
        plt.figure(figsize=(6, 4))
        y-=6
        x = int('32'+str(y))
    plt.subplot(x)
    plt.imshow(img)
    img = np.array(img)
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114])
    img = 255-img
    img = img / 255.
    img = np.reshape(img, (1, 28, 28, 1))
    plt.title('Result '+ str(np.argmax(model.predict(img))))
    plt.subplots_adjust(wspace=0.2, hspace=0.9)
plt.show()


#model.predict(img)