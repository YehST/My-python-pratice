#Curve Fitting
import numpy as np
import matplotlib.pyplot as plt

def read_data(datafile_name):
    # read from txt
    data = np.loadtxt('python\\Deep_Learning\\DL_IngJeng\\' +
                      datafile_name+'.csv',delimiter=',') #from vscode root directory
    n = len(data[:, 0])
    x = data[:, 0]
    y = data[:, 1]
    return n, x, y

def para_calculation(n, x, y):
    n_poly = 9 # n degree polynomial equation (1~9)
    y_ex = [0 for i in range(n_poly)] #intialize list to storage data
    sy2 = [0 for i in range(n_poly)]
    sy = [0 for i in range(n_poly)]
    y_eq = ['' for i in range(n_poly)]
    print("Standard Deviation：")
    for i in range(1,n_poly+1):
        z = np.polyfit(x, y, i)
        for j in range(0,i+1):
            y_ex[i-1] += z[-(j+1)] * (x**j) 
            y_eq[i-1] += '+(' + str(z[-(j+1)]) + ')x^' + str(j)
        sy2[i-1] = np.sum((y_ex[i-1]-y)**2)/(n-(n_poly+1))
        sy[i-1] = sy2[i-1]**0.5
        print(i,"degree :",sy[i-1]) #print standard deviation 
    [print('<',i,'equation > :',y_eq[i-1]) for i in range(1,n_poly+1)] #print polynomial eq
    return n_poly, y_ex

def main():
    datafile_name = 'data_of_poly2' #input("Enter the data file name:")
    n, x, y = read_data(datafile_name)
    n_poly, y_expected = para_calculation(n, x, y)
    plt.figure('Curve Fitting',figsize=(12, 6))
    for i in range(n_poly):
        plt.subplot(int('1'+str(n_poly)+str(i+1)))
        plt.xlabel('x', fontsize=12), plt.ylabel('y', fontsize=12)
        plt.xlim(0, 14), plt.ylim(0, 14)
        plt.title(str(i + 1) +' degree', fontsize=10)
        plt.grid(True, which='both')
        plt.plot(x, y, 'bs', markerfacecolor='none', label='measure datas')
        plt.plot(x, y_expected[i], 'g', label='fitting line')
        plt.legend(loc='lower right', prop={'size': 8})

main()
plt.show()