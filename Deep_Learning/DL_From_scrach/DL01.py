from ReferenceData.dataset.mnist import load_mnist
import sys
import os
import numpy as np
from PIL import Image
sys.path.append(os.pardir)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[1]
label = t_train[1]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)
