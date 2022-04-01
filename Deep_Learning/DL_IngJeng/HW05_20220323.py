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
    
def Polyfit(n_poly, n, x, y):
    return np.polyfit(x, y, n_poly)

def Pseudoinverse(n_poly, n, x, y):
    a = np.ones([n_poly + 1, n])
    for i in range(n_poly):
        a[i] = x ** (n_poly-i)
    p = np.zeros([1, n_poly + 1])
    X = np.transpose(a)
    Y = np.transpose(y)
    p = np.transpose(p)
    XT = np.transpose(X)
    XXTinv = np.linalg.inv(np.dot(XT, X))
    p = np.dot(np.dot(XXTinv, XT), Y)
    return p

def InverseM(n_poly, n, x, y):
    a = np.ones([n_poly + 1, n])
    for i in range(n_poly):
        a[i] = x ** (n_poly-i)
    x = [a.T[0], a.T[20], a.T[39]]
    y = [y[0], y[20], y[39]]
    p = np.zeros([1, n_poly + 1])
    p = np.dot(np.linalg.inv(x), y)
    return p
    
def main():
    Solution = {}
    Solution['Polyfit'], Solution['Pseudoinverse'], Solution['InverseM'] = {}, {}, {}
    n_poly = 2 #determine the n degree polynomial equation
    datafile_name = 'data_of_poly2' #input("Enter the data file name:")
    n, x, y= read_data(datafile_name)
    Solution['Polyfit']['para'] = Polyfit(n_poly, n, x, y)
    Solution['Pseudoinverse']['para'] = Pseudoinverse(n_poly, n, x, y)
    Solution['InverseM']['para'] = InverseM(n_poly, n, x, y)
    i=1
    plt.figure(figsize=(18, 6))
    for key in Solution.keys():
        Solution[key]['y_ex'] = 0
        Solution[key]['y_eq'] = ''
        for j in range(0,n_poly+1):
            Solution[key]['y_ex'] += Solution[key]['para'][j] * (x**(n_poly-j)) 
            Solution[key]['y_eq'] += '+ (' + str(round(Solution[key]['para'][j], 5)) + ')x^' + str(n_poly - j) + ' '
        sy2 = np.sum((Solution[key]['y_ex']-y)**2)/(n-(n_poly+1))
        Solution[key]['sy'] = sy2**0.5
        print('','='*(len(key)+6), '\n ||', key, '||\n','='*(len(key)+6))
        print(' equation：', Solution[key]['y_eq'])
        print(' Standard deviation：%f\n'%Solution[key]['sy']) 
        plt.subplot(int('13'+str(i)))
        plt.xlabel('x', fontsize=12), plt.ylabel('y', fontsize=12) 
        plt.xlim(0, 14), plt.ylim(0, 14) 
        plt.title(key, fontsize=10) 
        plt.grid(True, which='both') 
        plt.plot(x, y, 'bs', markerfacecolor='none') 
        plt.plot(x, Solution[key]['y_ex'], 'g') 
        i+=1
    plt.show()
main()