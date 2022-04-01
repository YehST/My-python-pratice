from typing_extensions import Self
from Basic import Act_Func, Loss_Func, Gradient
import sys
import os
import numpy as np

class simpleNet:
    def __init__(self):
        #self.W = np.random.randn(2,3)
        self.W = np.array([[0.47355232, 0.9977393, 0.84668094]
                        ,[0.85557411, 0.03563661, 0.69422093]])

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = Act_Func.softmax(z)
        loss = Loss_Func.cross_entropy_error(y, t)

        return loss

net = simpleNet()
print(net.W)
x= np.array([0.6, 0.9])
p = net.predict(x)
print(p) #[1.05414809 0.63071653 1.1328074 ]

t = np.array([0, 0, 1]) #Correct answer
print(net.loss(x, t)) #0.9280682857864075

f = lambda W:net.loss(x, t)
dW = Gradient.numerical_gradient(f, net.W)
print(dW) #[[ 0.21924757  0.14356243 -0.36281   ]
            #[ 0.32887136  0.21534364 -0.544215  ]]

