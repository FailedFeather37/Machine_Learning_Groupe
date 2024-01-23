import math
import random

b= 1
y=1
n=2



def tan_hyperbolique(x):
     cosh = (math.exp(x) + math.exp(-x)) / 2
     sinh = (math.exp(x) - math.exp(-x)) / 2
     tanh = sinh / cosh
     return tanh


def data_set():
     x=0
     l=[]
     for i in range(n):
        x = random.uniform(0,1)
        l.append(x)
     return(l)

print(data_set())

def poids():
    l=[]
    for i in range(n):
        x= random.uniform(1,10)
        l.append(x)
    return(l)

print(poids())


def somme_data_poids():
    liste_poids=poids()
    liste_data=data_set()
    a=0
    compt=0
    for i in liste_data:
        for x in liste_poids:
            produit=i*x
            a+=produit
            compt+=1
            if compt==n:
                return(a+b)
    return(a)


def somme_data_poids():
    liste_poids=poids()
    liste_data=data_set()









def f_complexe():
     f= somme_data_poids()
     estimation_tan=tan_hyperbolique(f)
     return estimation_tan

print(f_complexe())

def erreur():
    y_estimation=f_complexe()
    f_erreur=(y_estimation-y)**2
    return f_erreur



print(erreur())













