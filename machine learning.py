import math
import random

#ptites fonctions sigmoid tangente hyperpolique et leurs dérivé
def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig


def dev_sigmoid(x):
    dev_sig = math.exp(x) / (math.exp(x) + 1)
    return dev_sig


def tan_hyperbolique(x):
     cosh = (math.exp(x) + math.exp(-x)) / 2
     sinh = (math.exp(x) - math.exp(-x)) / 2
     tanh = sinh / cosh
     return tanh

def dev_tan_hyperbolique(x):
    dev_tanh = (math.exp**2(x) - 1)/(math.exp**2(x) + 1)
    return dev_tanh




#ptite fonction qui genere des nombre aléatoire entre 0 et 1
def aléatoire():

     x=0

     y=0
     l=[]
     for i in range(100):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        l.append(x)
        l.append(y)
     return l
print(aléatoire())

#ça c'est la partie de mael
















