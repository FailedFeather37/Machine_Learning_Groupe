﻿import math
import random

b= 1
y=1
n=10


def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig


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





def poids():
    l=[]
    for i in range(n):
        w= random.uniform(0,1)
        l.append(w)
    return(l)


def cible():
    y_cible=[]
    compt=0
    liste_cible=[]
    x=[0.2650378378515823, 0.9747940579528501, 0.30093636456233563, 0.15625866394225896, 0.9191197177833633, 0.005728140291855532, 0.9464320022425623, 0.6934330256004765, 0.44841333451904075, 0.1273259464305001]
    for i in x:
        compt+=1
        compt=compt % 2
        print(compt)
        if compt==1:
            x1=i
            liste_cible.append(x1)
        else:
            x2=i
            liste_cible.append(x2)
    compt2=0
    liste_somme=[]
    somme=0
    for i in liste_cible:
        compt2= compt2 % 2
        if compt2==0:
            somme+=i
            compt2+=1
        if compt2==1:
            somme+=i
            compt2+=1
            liste_somme.append(somme)
            somme=0
    return(liste_somme)



    return y_cible


# fonction permettant de faire f(X,W)=x1w1+x2w2 en faisant des paires avec x1 et x2 et en repetant ca n/2 fois
# return une liste avec a chaque fois x1w1+x2w2
def somme_data_poids(liste_data,liste_poids):
    a=0
    compt=1
    paire=0
    liste_paire=[]
    for i in range(n):
        produit=liste_poids[i]*liste_data[i]
        #print('produit {:d} : '.format(compt), produit,paire)
        if paire!=2:
            a+=produit
        else:
            liste_paire.append(a)
            a=liste_poids[i]*liste_data[i]
            paire=0

        if liste_poids[i]*liste_poids[i]==liste_poids[-1]*liste_poids[-1] and paire==1:
            liste_paire.append(a)

        if liste_poids[i]*liste_poids[i]==liste_poids[-1]*liste_poids[-1] and paire==0:
            liste_paire.append(a)
        paire+=1
        compt+=1

    return(liste_paire)



#Liste des estimations
def f_complexe():
     f= somme_data_poids(liste_data,liste_poids)
     liste_estimation=[]
     for i in f:
        estimation=sigmoid(i+b) # rajout du billet
        liste_estimation.append(estimation)
     return (liste_estimation)



#Liste des erreurs des estimations
def erreur():
    liste_estimation=f_complexe()
    liste_erreur=[]
    for i in liste_estimation:
        f_erreur=(i-y)**2
        liste_erreur.append(f_erreur)
    return (liste_erreur)




if __name__=="__main__":
    liste_poids=[0.5458182081873952, 0.7677241560346579, 0.6428221785941135, 0.09596345818777541, 0.3203503233887256, 0.6664673063819693, 0.5309717364821969, 0.7669344162937329, 0.6160847890715457, 0.7298075899016493]
    liste_data=[0.2650378378515823, 0.9747940579528501, 0.30093636456233563, 0.15625866394225896, 0.9191197177833633, 0.005728140291855532, 0.9464320022425623, 0.6934330256004765, 0.44841333451904075, 0.1273259464305001]
    print("Data_set : ",liste_data)
    print("Poids : ",liste_poids)
    print("somme_data_poids(): ",somme_data_poids(liste_data,liste_poids))
    print("f_complexe() : ",f_complexe())
    print("erreur() : ",erreur())

    print(cible())









