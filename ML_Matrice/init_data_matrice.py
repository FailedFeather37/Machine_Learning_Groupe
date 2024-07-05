import math
import numpy as np
from h5py import *



n_data=100
b=1


X= np.random.randint(0,2,size=(n_data,2))
X_analyse=np.random.randint(0,2,size=(n_data,2))

W=np.random.uniform(1,10,size=2)

print(X.shape,X)
print(W)




#Z = prediction
"""
facultatif : ce fait dans le neurone

Z=[]
for i in range(len(X)):
    z=X[i].dot(W)+b

    z=sigmoid(z)
    print(z)
    Z.append(z)

print(Z)
"""

#L = cible

def cible(X):
    L=[]
    for i in X:
        if i[0]+i[1]>0:
            L.append(1)
        else:
            L.append(0)
    return L



def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig



L=cible(X)
L_analyse=cible(X_analyse)
print(L_analyse)