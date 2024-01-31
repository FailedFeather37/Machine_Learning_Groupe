from math import *
import random

b= 1
y=1
n=2
assert n>=2, "n pas assez grand"

def sigmoid(x):
    sig = 1 / (1 + exp(-x))
    return sig


def tan_hyperbolique(x):
     cosh = (exp(x) + exp(-x)) / 2
     sinh = (exp(x) - exp(-x)) / 2
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
    w=0
    for i in range(n):
        w= random.uniform(-1,1)
        l.append(w)
    return(l)


# fonction permettant de faire f(X,W)=x1w1+x2w2 en faisant des paires avec x1 et x2 et en repetant ca n/2 fois
# return une liste avec a chaque fois x1w1+x2w2
def somme_data_poids():
    liste_poids=poids()
    liste_data=data_set()
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
     f= somme_data_poids()
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
        if i >=0.5:
            y=1
        else:
            y=0
        f_erreur=(i-y)**2
        liste_erreur.append(f_erreur)
    return (liste_erreur)

def test():
    liste_poids=[0.9780739719902576, -0.22117172174350075]
    liste_data=[0.07755742352567485, 0.09655479232859454]
    z=liste_poids[0]*liste_data[0]+liste_poids[1]*liste_data[1]+b
    z_sig=sigmoid(z)
    erreur=(1-z_sig)**2
    return(erreur)
    

if __name__=="__main__":
    
    print("Data_set : ",data_set())
    print("Poids : ",poids())
    print("somme_data_poids(): ",somme_data_poids())
    print("f_complexe() : ",f_complexe())
    print("erreur() : ",erreur())
    
    #print(test())











