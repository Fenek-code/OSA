import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import random

def easy_function(x):
    return(1/x)

X=np.linspace(-20,20,1000)
plt.plot(X,easy_function(X))
plt.show()
def MCint_area_vec(f, a, b, m, N):
    x = random.uniform(a, b, N)
    y = random.uniform(0, m, N)
    M = y[y < f(x)].size # в квадратных скобках условие,
    # size считает число ему удовлетворяющих элементов
    area = M/float(N)*m*(b-a)
    return area

print("S = ", MCint_area_vec(easy_function, 0,2,100,1000))

def integrate(x1,x2,func=easy_function,n=100000):
    X=np.linspace(x1,x2,1000)
    y1=0
    y2=max((func(X)))+1
    print(x1,x2,y1,y2)
    area=(x2-x1)*(y2-y1)
    check=[]
    xs=[]
    ys=[]
    for i in range(n):
        x=np.random.uniform(x1,x2,1)
        xs.append(x)
        y=np.random.uniform(y1,y2,1)
        ys.append(y)
        if abs(y)>abs(func(x)) or y<0:
            check.append(0)
        else:
            check.append(1)
    return(np.mean(check)*area,xs,ys,check)

print(integrate(1,3)[0])
_,x,y,c=integrate(1,3,n=100)
df=pd.DataFrame()
df['x']=x
df['y']=y
df['c']=c

X=np.linspace(1,3,1000)
plt.plot(X,easy_function(X))
plt.scatter(df[df['c']==0]['x'],df[df['c']==0]['y'],color='red')
plt.scatter(df[df['c']==1]['x'],df[df['c']==1]['y'],color='blue')
plt.show()
