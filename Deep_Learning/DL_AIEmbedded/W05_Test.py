import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#版本需相同
model = tf.keras.models.load_model(r'D:\vscode\python\Deep_Learning\DL_AIEmbedded\Model\MNIST_LeNet\Adam\lr0035_Dropout_PerformanceScheduling_30e\Tahn_Ver\mnist_Lenet.h5')

fig,axs = plt.subplots(5,2)
for i in range(10):
    im = Image.open(f'.\\python\\Deep_Learning\\DL_AIEmbedded\\number_data\\number_PNG/{i}.png')
    img = np.array(im)
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114])
    img = 255-img
    img = img / 255.
    img = np.reshape(img, (1, 28, 28, 1))
    if i >= 5:
        axs[i-5,1].imshow(im)
        axs[i-5,1].set_title('Result '+ str(np.argmax(model.predict(img))))
    else:
        axs[i,0].imshow(im)
        axs[i,0].set_title('Result '+ str(np.argmax(model.predict(img))))
    fig.tight_layout()
    
plt.show()


#model.predict(img)