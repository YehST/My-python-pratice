from dataset.mnist import load_mnist
import numpy as np
from PIL import Image
import random
import pickle
from Basic import Act_Func


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def get_data(flatten=False, normalize=False, one_hot_label=False):
    (x_train, L_train), (x_test, L_test) = load_mnist(
        flatten=flatten, normalize=normalize, one_hot_label=one_hot_label)
    return x_test, L_test, x_train, L_train


def init_network():
    with open(r"D:\vscode\python\Deep_Learning\DL_From_scrach\ReferenceData\ch03\sample_weight.pkl", 'rb') as f:
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
    y = Act_Func.softmax(a3)

    return y


def main():
    x_test, L_test, x_train, L_train = get_data(
        flatten=False, normalize=False, one_hot_label=False)
    print('\nx Train：', np.shape(x_train))
    print('Label Train：', np.shape(L_train))
    print('x Test：', np.shape(x_test))
    print('Label Test：', np.shape(L_test))

    x = random.randint(0, 9999)
    img = x_train[x]
    label = L_train[x]
    print('\nImage shape', img.shape)
    img = img.reshape(28, 28)
    img_show(img)


def main3():
    x_test, L_test, x_train, L_train = get_data(
        flatten=False, normalize=False, one_hot_label=False)
    network = init_network()
    x = random.randint(0, 9999)
    # x = input('0~9999')
    print('The', x, 'data of test')
    img = x_test[x]
    Label = L_test[x]
    y = predict(network, x_test[x].flatten())
    print(y)
    print(Label)
    y = np.argmax(y)
    Label = np.argmax(Label)
    '''
    print('Label：%d\nPredict：%d' % (Label, y))
    if Label == y:
        print('Correct！')
    else:
        print('Mistake')
    print('\nImage shape', img.shape)
    img = img.reshape(28, 28)
    img_show(img)
    '''


main3()
# normalize = True ---> 會將灰階值0~255轉換為0~1，造成將圖輸出後會顯示全黑，這是因為原本灰階值越接近255會越白，normalize後變成0~1幾乎為全黑
# flatten = True ---> 會將陣列資料打成一維，若無此動作，將無法將資料丟入模型中預測
# one_hot_label ---> 讓label變成10個2進位資料，1的位置即為其資料正確數字
