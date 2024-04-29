import math
import random
import matplotlib.pyplot as plt
import numpy as np


b=0

input=int(input("Combien de données ? :"))
n_data=input
#n_data=100
n2_data=int(n_data/2)

#n_data_analyse=100
n_data_analyse=input
n2_data_analyse=int(n_data_analyse/2)
assert input>=10, "Nombre insuffisant de données"


def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig


#Génération des données pour l'apprentissage
def data_set():
     x=0
     l=[]
     for i in range(n_data):
        x = random.uniform(0,1)
        l.append(x)
     l_pour_somme=l
     l=liste_tuple(l,2)
     return(l_pour_somme,l)


#Nouvelles données pour analyse
def data_analyse():
     l=[]
     for i in range(n_data_analyse):
        x = random.uniform(0,1)
        l.append(x)
     l_pour_somme=l
     l=liste_tuple(l,2)
     return(l_pour_somme,l)


def poids():
    l=[]
    for i in range(2):
        w= random.uniform(0,10)
        l.append(w)
    return(l)


# fonction permettant de faire le produit scalaire de w et x : f(X,W)=x1w1+x2w2 en faisant des paires avec x1 et x2 et en repetant ca n/2 fois
# return une liste avec chaque  x1w1+x2w2
def somme_data_poids(liste_data, liste_poids,n_data):
    liste_paire = []
    for i in range(n_data):
        produit = liste_poids[0] * liste_data[i] + liste_poids[1] * liste_data[i]
        liste_paire.append(produit)
    return liste_paire


#ciblage des x1 et x2
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


#Somme des cible de x1 et x2
#Ciblage pour le ET logique
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


#sur-echantillonage des données
def equilibrage(liste_cible_max,liste_data_pour_somme,n_data):
    pourc0,pourc1=perc(liste_cible_max)
    while pourc1 !=50 or pourc0!=50:
        for j in range(2):
            x = random.uniform(0.5,1)
            liste_data_pour_somme.append(x)  
            n_data+=1
        if pourc1 < 50:
            liste_cible_max.append(1)
        else:
            liste_cible_max.append(0)
        pourc0,pourc1=perc(liste_cible_max)
    liste_data_pour_somme=liste_tuple(liste_data_pour_somme,2)
    return (liste_cible_max,liste_data_pour_somme,n_data)


#Liste des estimations
def f_complexe(somme):
     liste_estimation=[]
     for i in somme:
        # rajout de l'estimation + le billet
        estimation=sigmoid(i+b)
        liste_estimation.append(estimation)
     return (liste_estimation)


#Liste des erreurs des estimations
def erreur(liste_cible_max,f_xw):
    a=0
    liste_estimation=f_xw
    liste_erreur=[]
    for i in liste_estimation:
        f_erreur=(liste_cible_max[a]-i)**2
        a=+1
        liste_erreur.append(f_erreur)
    return (liste_erreur)


def tuple_vers_liste(liste):
    l=[]
    for i in liste:
       l.append(i[0])
       l.append(i[1])
    return(l) 


def affichage_point():
    #Affichage des x1/x2 learn
    liste_x1=[]
    liste_x2=[]
    for i in range(n2_data):
        x1=liste_data[i][0]
        x2=liste_data[i][1]
        liste_x1.append(x1)
        liste_x2.append(x2)
    x_point=np.linspace(0,len(liste_cible_max),len(liste_cible_max))
    plt.scatter(x_point,liste_cible_max)
    plt.title("Affichage des points x1 et x2 lors du listage")
    plt.show()


#PREPARATION DES DONNEES POUR L'APPPRENTISSAGE
# liste_data_pour_somme --> sans tuple
# liste_data --> avec tuple
liste_data_pour_somme,liste_data=data_set()
liste_poids=poids()

#cible pour chaque x
liste_cible=cible(liste_data)

#cible des ET logique (0 ou 1 pour une paire de x1 et x2)
liste_cible_max=cible_somme(liste_cible)

#maj/equilibrage des cibles et de la liste de données
liste_cible_max,liste_data,n_data=equilibrage(liste_cible_max,liste_data_pour_somme,n_data)

#maj de la 2e liste en fonction de la 1er
liste_data_pour_somme=tuple_vers_liste(liste_data)

#produit des données mis à jour et des poids
somme_learn=somme_data_poids(liste_data_pour_somme,liste_poids,n_data)


#PREPARATION DES DONNEES POUR L'ANALYSE
#Génération de nouvellles données pour l'analyse
liste_data_analyse_pour_somme,liste_data_analyse=data_analyse()

#cible des x des données de l'analyse
liste_cible_analyse=cible(liste_data_analyse)

#cible des paires de l'analyse
liste_cible_max_analyse=cible_somme(liste_cible_analyse)

#maj/equilibrage des cibles et de la liste de données de l'analyse
liste_cible_max_analyse,liste_data_analyse,n_data_analyse=equilibrage(liste_cible_max_analyse,liste_data_analyse_pour_somme,n_data_analyse)

#maj data somme analyse
liste_data_analyse=tuple_vers_liste(liste_data_analyse)
liste_data_analyse=liste_tuple(liste_data_analyse,2)

#produit des données de l'analyse mis à jour et des poids
somme_analyse=somme_data_poids(liste_data_analyse_pour_somme,liste_poids,n_data_analyse)

#FONCTION ET ERREURS
#Data Learn
f_xw_learn=f_complexe(somme_learn)
liste_erreur=erreur(liste_cible_max,f_xw_learn)
#print("f(X,W) learn :",f_xw_learn)
#print("liste d'erreur learn :",liste_erreur)

#Affichage des points pour l'apprentissage
#print(affichage_point())

#Analyse
f_xw_analyse=f_complexe(somme_analyse)
liste_erreur_analyse=erreur(liste_cible_max_analyse,f_xw_analyse)
#print("f(X,W) analyse :",f_xw_analyse)
#print("liste d'erreur analyse :",liste_erreur_analyse)