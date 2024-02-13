import math
import random
import matplotlib.pyplot as plt
import numpy as np



b= 1
n=4
n2=int(n/2)


def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig


def data_set():
     x=0
     l=[]
     for i in range(n):
        x = random.uniform(0,1)
        l.append(x)
     l_pour_somme=l
     l=liste_tuple(l,2)
     return(l_pour_somme,l)
 
 
#nouvelles données pour analyse
def data_analyse():
     l=[]
     for i in range(n):
        x = random.uniform(0,1)
        l.append(x)
     
     l=liste_tuple(l,2)
     return(l) 


 
def poids():
    l=[]
    for i in range(2):
        w= random.uniform(0,10)
        l.append(w)
    return(l)



# fonction permettant de faire le produit scalaire de w et x : f(X,W)=x1w1+x2w2 en faisant des paires avec x1 et x2 et en repetant ca n/2 fois
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

"""
def somme_data_poids(liste_data, liste_poids):
    liste_paire = []
    for i in range(n):
        produit = liste_poids[0] * liste_data[i] + liste_poids[1] * liste_data[i]
        liste_paire.append(produit)
    return liste_paire
"""

def cible(liste_data):
    liste_cible=[]
    for i in liste_data:
        for j in range(2):
            if i[j]<0.5:
                liste_cible.append(0)
            else:
                liste_cible.append(1)
    return (liste_cible)


def liste_tuple(liste, taille_tuple):
    liste_de_tuples = []
    for i in range(0, len(liste), taille_tuple):
        sous_liste = liste[i:i + taille_tuple]
        tuple_courant = tuple(sous_liste)
        liste_de_tuples.append(tuple_courant)

    return liste_de_tuples


def cible_somme(liste_cible):
    cible=[]
    compt1=0
    compt0=0
    liste_cible=liste_tuple(liste_cible,2)
    for i in liste_cible:
        if i[0]+i[1]==2:
            cible.append(1)
            compt1+=1
        else:
            cible.append(0)
            compt0+=1
    return cible


def comptage(liste_cible_max):
    compt1=0
    compt0=0
    for i in liste_cible_max:
        if i==0:
            compt0+=1
        else:
            compt1+=1
    return (compt0,compt1)


#pourcentage de 1 et de 0 dans la liste de cible pour les paires de x1x2
def perc(liste_cible_max):
    compt0,compt1=comptage(liste_cible_max)
    pourc1=int(compt1*100/len(liste_cible_max))
    pourc0=int(compt0*100/len(liste_cible_max))
    return pourc0,pourc1

#sur echantillonage des données
def equilibrage(liste_cible_max,liste_data_pour_somme):
    pourc0,pourc1=perc(liste_cible_max)
    while pourc1 !=50 or pourc0!=50:
        for j in range(2):
            x = random.uniform(0.5,1)
            liste_data_pour_somme.append(x)
        if pourc1 < 50:
            liste_cible_max.append(1)
        else:
            liste_cible_max.append(0)
        pourc0,pourc1=perc(liste_cible_max)
    liste_data_pour_somme=liste_tuple(liste_data_pour_somme,2)
    return (liste_cible_max,liste_data_pour_somme)    


#Liste des estimations
def f_complexe(somme):
     liste_estimation=[]
     for i in somme:
        estimation=sigmoid(i+b) # rajout du billet
        liste_estimation.append(estimation)
     return (liste_estimation)


#Liste des erreurs des estimations
def erreur(liste_cible_max):
    a=0
    liste_estimation=f_complexe(somme)
    liste_erreur=[]
    for i in liste_estimation:
        f_erreur=(liste_cible_max[a]-i)**2
        a=+1
        liste_erreur.append(f_erreur)
    return (liste_erreur)


# liste_data_pour_somme --> sans tuple
# liste_data --> avec tuple
liste_data_pour_somme,liste_data=data_set()
print(liste_data_pour_somme,liste_data)
liste_poids=poids()

if __name__=="__main__":
    print("data_set() : ",liste_data)
    print("poids() : ",liste_poids)
    liste_cible=cible(liste_data)
    print("cible des ET logique (0 ou 1 pour une paire de x1 et x2) :",cible_somme(liste_cible))
    
liste_cible_max=cible_somme(liste_cible)

print("somme_data_poids(liste_data,liste_poids): ",somme_data_poids(liste_data_pour_somme,liste_poids))

liste_cible_max,liste_data=equilibrage(liste_cible_max,liste_data_pour_somme)

print(equilibrage(liste_cible_max,liste_data_pour_somme))



#print(liste_data_pour_somme,"ah")

somme=somme_data_poids(liste_data_pour_somme,liste_poids)
print(somme)

print("f_complexe(somme) : ",f_complexe(somme))

print("erreur(liste_cible) : ",erreur(liste_cible))


"""
liste_x1=[]
liste_x2=[]
for i in range(n2):
    x1=liste_data[i]
    x2=liste_data[i:i+1]
    x2=x2[0]
    liste_x1.append(x1)
    liste_x2.append(x2)
x_point=np.linspace(0,len(liste_cible_max),len(liste_cible_max))
plt.scatter(x_point,liste_cible_max)
plt.show()


"""



