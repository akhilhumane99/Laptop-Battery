#Akhil Humane
#PRN:10303320171124510016


import numpy as np
import pandas as pd 
from matplotlib import pyplot
import pylab

X,Y = np.loadtxt('https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt', delimiter=',',unpack=True)
x=pd.Series(X)
y=pd.Series(Y)
r= x.cov(y)/(y.std()*x.std())
b1= r*y.std()/x.std()
b0= y.mean()-(b1*x.mean())

pyplot.scatter(x,y)
pyplot.title('Laptop Battery Chart')
pyplot.xlabel('Charging')
pyplot.ylabel('Screen_ime')
pyplot.grid()
pyplot.show()

new=float(input())
res=round(b1*new+b0,2)
print(res)
