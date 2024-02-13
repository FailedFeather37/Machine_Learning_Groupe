from init_data import *
from deriv import *
from math import *
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
#from tqdm import tqdm
import numpy as np



learning_rate=0.2
liste_learn=[]
EPOCHS=100
y_learn_liste=[]


class Neurone:
    def __init__(self): #1 init
        self.w1=liste_poids[0]
        self.w2=liste_poids[1]
        self.b=b

    #2 calcul prediction selon x1 et x2 (class)
    def prediction(self,x1,x2):
        neg=Variable(-1)
        neg=Variable(-1)
        sig_value1=Variable(1)


        self.x1_g = Variable(x1)
        self.x2_g = Variable(x2)
        self.w1_g = Variable(self.w1)
        self.w2_g = Variable(self.w2)
        self.b_g = Variable(self.b)

        z=self.x1_g*self.w1_g+self.x2_g*self.w2_g + self.b_g

        z_neg=z*neg
        #gradient sigmoid
        z_sig= sig_value1 / (sig_value1 + z_neg.exp())

        return z_sig


    #3 calcul de l'erreur avec les variables
    def erreur(self,z_sig,i):
        pui=Variable(2)
        cible_object=Variable(liste_max_cible[i])
        #gradient erreur
        e = (cible_object - z_sig)**pui
        return e


     #derive partiel avec E
    def apprentissage(self):
        E=0
        y_learn_liste=[]
        #print("Estimations learn class")
        for i in range(n2):
            x1=liste_data[i]
            x2=liste_data[i:i+1]
            x2=x2[0]
            self.x1_g = Variable(x1)
            self.x2_g = Variable(x2)
            z_sig = self.prediction(x1,x2)
            e = self.erreur(z_sig,i)
            # boucle pour x1 et x2

            #nouvelle méthode
            # dérivées partielles
            de_dw1=calcul_gradient(e,self.w1_g)
            de_dw2=calcul_gradient(e,self.w2_g)
            de_db=calcul_gradient(e,self.b_g)

            # maj des valeurs avec les gradients
            self.w1 = self.w1-learning_rate*de_dw1
            self.w2 = self.w2-learning_rate*de_dw2
            self.b = self.b-learning_rate*de_db

            #recalcul des valeurs pour listage et modélisation
            z=x1*self.w1+x2*self.w2+b
            z=sigmoid(z)

            #calcul erreur : (y1' - y1)**2
            e = (z - liste_max_cible[i])**2
            E+=e/EPOCHS
            #print(self.w1,self.w2,self.b,e,z)

        #print("Accuracy Score:", accuracy_score(liste_max_cible,y_learn_liste))
        return E


    #analyse de l'apprentissage avec un nouveau E et nouvelles datas
    def analyse(self):
        E_analyse=0
        y_liste=[]
        for x in range(n2):
            x1=liste_analyse[x]
            x2=liste_analyse[x:x+1]
            x2=x2[0]

            z=x1*self.w1+x2*self.w2+b

            z=sigmoid(z)

            #calcul erreur de l'analyse
            e = (z - liste_max_cible[x])**2

            if z >=0.5:
                y_liste.append(1)
            else:
                y_liste.append(0)

            E_analyse+=e/EPOCHS

        #Evaluation de la précision du modèle
        print("Accuracy Score analyse :", accuracy_score(liste_cible_analyse,y_liste))
        print(liste_max_cible)
        print(y_liste)
        return E_analyse


    def exec(self):
        liste_E=[]
        for i in (range(EPOCHS)):
            learn=self.apprentissage()
            liste_E.append(learn)
        return liste_E


if __name__=="__main__":
    neurore=Neurone()
    liste_analyse=data_analyse()
    liste_cible_analyse=paire_cible(cible(liste_analyse))

    liste_E=neurore.exec()
    analyse=neurore.analyse()
    print("E de l'analyse :",analyse)
    x_points=np.linspace(0,EPOCHS,EPOCHS)
    plt.plot(x_points,liste_E)
    plt.ylabel('erreurs')
    plt.title('Evolution de l\'erreur E '
    'en fonction du nombre des EPOCHS')
    #plt.show()

#corriger vrai et equilibrer données




"""

afficher les x1 et x2

faire une courbe roc ?
faire quantile pour seuil de classification ?
methode pour derive partielle et calcul de l'erreur
"""
"""
1. __init__ avec les poids (class)
2. calcul prediction selon x1 et x2 (class)
3. calcul de l'erreur avec les variables  ( dans main)
4. apprentissage avec E (class)
"""

"""
change valeur de x1 et x2 a chaque iteration
boucle for = E
1 estimation = 1 itération
(y1^-y1)²
(y2^-y2)²  --> E calcul gradient
(y3^-y3)²
(y3^-y3)²

((x1,x2),y1) --> y1^'
"""