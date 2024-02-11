import math
import random
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig

# peut changer avec tangente hyperbolique
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

"""
def affichage(liste_data):
    liste_x1=[]
    liste_x2=[]
    for i in range(n2):
        x1=liste_data[i]
        x2=liste_data[i:i+1]
        x2=x2[0]
        liste_x1.append(x1)
        liste_x2.append(x2)
    x_point=np.linspace(0,len(liste_max_cible),len(liste_max_cible))
    plt.scatter(x_point,liste_max_cible)
    plt.show()
"""        



#nouvelle données pour analyse
def data_analyse():
     l=[]
     for i in range(n):
        x = random.uniform(0,1)
        l.append(x)
     return(l)


def poids():
    l=[]
    for i in range(2):
        w= random.uniform(0,10)
        l.append(w)
    return(l)


# fonction permettant de faire f(X,W)=x1w1+x2w2 en faisant des paires avec x1 et x2 et en repetant ca n/2 fois
# return une liste avec a chaque fois x1w1+x2w2
def somme_data_poids(liste_data,liste_poids):
    a=0
    compt=1
    comptw=0
    paire=0
    liste_paire=[]
    ite=0
    for i in range(n):
        produit=liste_poids[comptw]*liste_data[i]
        if paire!=2:
            a+=produit
        else:
            liste_paire.append(a)
            a=liste_poids[comptw]*liste_data[i]
            paire=0
        if produit==liste_poids[ite]*liste_data[-1] and paire==1:
            liste_paire.append(a)

        if produit==liste_poids[ite]*liste_data[-1] and paire==0:
            liste_paire.append(a)
        paire+=1
        compt+=1
        comptw+=1
        comptw= comptw % 2
        ite=n-comptw
        ite=ite %2
    return(liste_paire)

#Liste des estimations
def f_complexe(somme): # changer nom avec estimation
     liste_estimation=[]
     for i in somme:
        estimation=sigmoid(i+b) # rajout du billet
        liste_estimation.append(estimation)
     return (liste_estimation)



#Liste des erreurs des estimations
def erreur(liste_max_cible):
    a=0
    liste_estimation=f_complexe(somme)
    liste_erreur=[]
    for i in liste_estimation:
        f_erreur=(liste_max_cible[a]-i)**2
        a=+1
        liste_erreur.append(f_erreur)
    return (liste_erreur)


def cible(liste_data):
    y_cible=[]
    compt=0
    liste_cible=[]
    for i in liste_data:
        if i<0.5:
            x1=0
            liste_cible.append(x1)
        else:
            x2=1
            liste_cible.append(x2)
    return(liste_cible)


def liste_tuple(liste, taille_tuple):
    liste_de_tuples = []

    for i in range(0, len(liste), taille_tuple):
        sous_liste = liste[i:i + taille_tuple]
        tuple_courant = tuple(sous_liste)
        liste_de_tuples.append(tuple_courant)

    return liste_de_tuples



def paire_cible(liste_cible):
    liste_cible=liste_tuple(liste_cible,2)
    cible=[]
    compt1=0
    compt0=0
    for i in liste_cible:
        if i[0]+i[1]==2:
            cible.append(1)
            compt1+=1
        else:
            cible.append(0)
            compt0+=1
    return cible


def comptage(liste_cible):
    liste_cible=liste_tuple(liste_cible,2)
    cible=[]
    compt1=0
    compt0=0
    for i in liste_cible:
        if i[0]+i[1]==2:
            cible.append(1)
            compt1+=1
        else:
            cible.append(0)
            compt0+=1
    return compt0,compt1


def perc(liste_max_cible): #reequilibrer x1 et x2
    nbr0,nbr1=comptage(liste_cible)
    perc0=int(nbr0*100/len(liste_max_cible))
    perc1=int(nbr1*100/len(liste_max_cible))
    return (perc0,perc1) 

def sur_echantillonage(liste_data):
    _,perc1=perc(liste_max_cible)
    liste_cible_maj=liste_max_cible
    for i in range(5):
        for i in range(n):
            for i in range(2):
                x = random.uniform(0.5,1)
                liste_data.append(x)
            liste_cible_maj.append(1)
            _,perc1=perc(liste_cible_maj)
        print(perc1)
        #print(liste_cible_maj)
    return(None)

# laisser si test avec des valeurs fixes
#liste_data=[0.2650378378515823, 0.9747940579528501, 0.30093636456233563, 0.15625866394225896, 0.9191197177833633, 0.005728140291855532]
#liste_poids=[0.5458182081873952, 0.7677241560346579, 0.6428221785941135, 0.09596345818777541, 0.3203503233887256, 0.6664673063819693]


b= 1
n=100 
n2=int(n/2)
liste_data=data_set()
liste_poids=poids()

if __name__=="__main__":
    #print("data_set() : ",liste_data)
    #print("poids() : ",liste_poids)
    #print(paire_cible(cible(liste_data)))
    #print("somme_data_poids(liste_data,liste_poids): ",somme_data_poids(liste_data,liste_poids))
    k=1

somme=somme_data_poids(liste_data,liste_poids)
#print("f_complexe(somme) : ",f_complexe(somme))

liste_cible=cible(liste_data)
liste_max_cible=paire_cible(liste_cible)
#print("erreur(liste_max_cible) : ",erreur(liste_max_cible))
erreur=erreur(liste_max_cible)
print(comptage(liste_cible))
print(perc(liste_max_cible))
#print(affichage(liste_data))
print(sur_echantillonage(liste_data)) 