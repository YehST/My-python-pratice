import numpy as np
import cv2
import tensorflow as tf

# 載入模型
#model = tf.keras.models.load_model('./tf_practice/model_test/AdaGrad/mnist_lenet.h5')
model = tf.keras.models.load_model(r'D:\vscode\python\Deep_Learning\DL_AIEmbedded\Model\mnist_Lenet_SGD\mnist_Lenet.h5')

for i in range(10):
    img = cv2.imread(f'.\\python\\Deep_Learning\\DL_AIEmbedded\\number_data\\number_PNG/{i}.png', -1)
    cv2.imshow(f'Number {i}', img)
    img = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    img = 255-img
    img = np.reshape(img, (1, 28, 28, 1))
    pred = np.argmax(model.predict(img))
    print(f'Photo: Number:{i}, Predict:{pred}')

cv2.waitKey()
cv2.destroyAllWindows()