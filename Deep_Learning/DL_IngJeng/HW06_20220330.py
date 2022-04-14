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
    with open(r"python\Deep_Learning\DL_From_scrach\ReferenceData\ch03\sample_weight.pkl", 'rb') as f:
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


def printM(M):
    rows = M.shape[0]
    cols = M.shape[1]
    for i in range(0, rows):
        str1 = ""
        for j in range(0, cols):
            str1 += ("%3.0f " % M[i, j])
        print(str1)
    print("")


def main():
    x = random.randint(0, 9999)
    print('\033[1mThe %d data of mnist dataset\033[0m' % x)
    for i in range(2):
        for j in range(2):
            x_test, L_test, x_train, L_train = get_data(
                flatten=i == 1, normalize=j == 1)
            print('\n\033[1m*flatten=%s, normalize=%s\033[0m' %
                  (i == 1, j == 1))
            print(' Train Img：', np.shape(x_train))
            print(' Test  Img：', np.shape(x_test))
            print(' Train Label：', np.shape(L_train))
            print(' Test  Label：', np.shape(L_test))

            img = x_test[x]
            img = img.reshape(28, 28)
            # printM(img)
            img_show(img)


def main3():
    network = init_network()
    x = int(input('Please choose a 0~9999 number:'))
    print('\033[1mThe %d data of test data\033[0m' % x)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                x_test, L_test, x_train, L_train = get_data(
                    flatten=i == 1, normalize=j == 1, one_hot_label=k == 1)
                print('\n\033[1m*flatten=%s, normalize=%s, one_hot_label=%s\033[0m' %
                      (i == 1, j == 1, k == 1))

                img = x_test[x]
                Label = L_test[x]
                y = predict(network, x_test[x].flatten())
                y = np.argmax(y)
                if k == 1:
                    print(' original label:', Label)
                    Label = np.argmax(Label)
                    print(' transfered label:', Label)

                print(' Label：%d\n Predict：%d' % (Label, y))
                if Label == y:
                    print('\033[1m Correct！\033[0m')
                else:
                    print('\033[91m Mistake! \033[0m')
                img = img.reshape(28, 28)
                img_show(img)


# normalize = True ---> 會將灰階值0~255轉換為0~1，造成將圖輸出後會顯示全黑，這是因為原本灰階值越接近255會越白，normalize後變成0~1幾乎為全黑
# flatten = True ---> 會將陣列資料打成一維，若無此動作，將無法將資料丟入模型中預測
# one_hot_label ---> 讓label變成10個2進位資料，1的位置即為其資料正確數字
