#Curve Fitting
import numpy as np
import matplotlib.pyplot as plt


def read_data(datafile_name):
    # read from txt
    data = np.loadtxt('python\\Deep_Learning\\DL_IngJeng\\' +
                      datafile_name+'.txt') #from vscode root directory
    n = len(data[:, 0])
    x = data[:, 0]
    y = data[:, 1]
    return n, x, y


def para_calculation(n, x, y):
    sum_x = 0
    for i in range(0, n):
        sum_x = sum_x + x[i]
    sum_y = 0
    for i in range(0, n):
        sum_y = sum_y + y[i]
    sum_xy = np.sum(x*y)
    sum_x2 = np.dot(x, x)
    m = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)
    b = (sum_y*sum_x2 - sum_xy*sum_x)/(n*sum_x2 - sum_x**2)

    y_expected = m*x+b
    sy2 = np.sum((y_expected-y)**2)/(n-2)
    sx2 = sy2/(m**2)
    sx = np.sqrt(sx2)
    return m, b, sx


def main():
    datafile_name = 'W02' #input("Enter the data file name:")
    n, x, y = read_data(datafile_name)
    m, b, sx = para_calculation(n, x, y)
    plt.figure(figsize=(10, 6))
    plt.title('Cruve fitting', fontsize=20)
    plt.xlabel('x', fontsize=12), plt.ylabel('y', fontsize=12)
    plt.xlim(0, 55), plt.ylim(0, 55)
    plt.grid(True, which='both')
    plt.plot(x, y, 'ro', markerfacecolor='none', label='measure datas')
    plt.plot(x, m*x+b, 'b', label='fitting line')
    plt.plot(x, m*(x+2*sx)+b, 'g:')
    plt.plot(x, m*(x-2*sx)+b, 'g:')
    plt.legend(loc='lower right', prop={'size': 16})

main()
plt.show()
