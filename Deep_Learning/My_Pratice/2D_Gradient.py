import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, solve, diff

def gradient2D(f, x):
    para_x = Symbol('x')
    f_diff = diff(f)
    grand = f_diff.subs({para_x:x})
    
    return grand

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_array= []
    for i in range(step_num):
        grad = gradient2D(f, x)
        x = x - lr * grad
        x_array.append(x)

    return x, x_array 

x = Symbol('x')
y = x**2 + 4*x + 4

xrange = np.arange(-10, 10, 1)
yrange = np.array([y.subs({x:i}) for i in xrange])

init_x = 10
ans, x_array = gradient_descent(y, init_x, 0.1, 1000)
print(ans) # -2.00000000000000

plt.plot(xrange, yrange, 'g')
plt.plot(ans, y.subs({x:ans}), 'ro')
for i in range(len(x_array)):
    plt.plot(x_array[i], y.subs({x:x_array[i]}),'r+')
plt.grid()
plt.show()