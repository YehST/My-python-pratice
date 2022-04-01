import numpy as np
import matplotlib.pyplot as plt
from Basic import Act_Func, Loss_Func

class simpleNet:
    def __init__(self):
        self.W = np.array([[0.47355232, 0.9977393, 0.84668094],
                        [0.85557411, 0.03563661, 0.69422093]])
    def predict(self, x):
        return np.dot(x, self.W)
    
    def loss(self, x, w, t):
        z = np.dot(x, w)
        y = Act_Func.softmax(z)
        loss = Loss_Func.cross_entropy_error(y, t)

        return loss

    def gradient(self, loss, w):
        h = 1e-4
        shape = w.shape
        grad = np.zeros(w.size)
        w = np.ravel(w)
        for i in range(w.size):
            tmp_val = w[i]

            w[i] = tmp_val + h
            tmp_array = np.reshape(w, shape)
            fxh1 = loss(W = tmp_array)
            
            w[i] = tmp_val - h
            tmp_array = np.reshape(w, shape)
            fxh2 = loss(W = tmp_array)
            
            grad[i] = (fxh1 - fxh2) / (2 * h)
            
            w[i] = tmp_val
        
        grad = np.reshape(grad, shape)
        return grad
# ============================================================
x = np.array([0.6, 0.9])
net = simpleNet()
p = net.predict(x)
t = np.zeros(p.size)
t[np.argmax(p)] = 1
print(t) # [0. 0. 1.]
loss = net.loss(x, net.W, t)
print(loss) # 0.9280682857864075

f = lambda W: net.loss(x, W, t)
dW = net.gradient(f, net.W)
print(dW)
# [[ 0.21924757  0.14356243 -0.36281   ]      
#  [ 0.32887136  0.21534364 -0.544215  ]]