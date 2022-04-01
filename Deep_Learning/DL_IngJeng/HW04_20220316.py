# Activation Function
import matplotlib.pyplot as plt
import numpy as np
from Basic import Act_Func

x = np.linspace(-5.0, 5.0, 10000)
x1 = [0.3, 2.9, 4.]
y = [Act_Func.step_func(x), Act_Func.relu(x), Act_Func.sigmoid(
    x), Act_Func.softplus(x), Act_Func.tahn(x)]
print('x =', x1)
print('softmax(x)=', Act_Func.softmax(x1))
plt.plot(x, y[0], 'b', label='step func')
plt.plot(x, y[1], 'r', label='relu')
plt.plot(x, y[2], 'g', label='sigmoid')
plt.plot(x, y[3], 'y', label='softplus')
plt.plot(x, y[4], 'k', label='tahn')
plt.grid(True, which='both')
plt.ylim(-2.0, 6.0), plt.xlim(-6.0, 6.0)
plt.legend(loc='upper left', prop={'size': 12})
plt.show()
