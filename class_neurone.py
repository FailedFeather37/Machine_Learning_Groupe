from init_data import *
from deriv import *
from math import *
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from tqdm import tqdm
import numpy as np



learning_rate=0.2
liste_learn=[]
EPOCHS=400
y_learn_liste=[]
compt=0

class Neurone:
    #initialisation
    def __init__(self):
        self.w1=liste_poids[0]
        self.w2=liste_poids[1]
        self.b=b

    #calcul de la prediction selon x1 et x2 (class)
    def prediction(self,x1,x2):
        neg=Variable(-1)
        sig_value1=Variable(1)

        self.x1_g = Variable(x1)
        self.x2_g = Variable(x2)
        self.w1_g = Variable(self.w1)
        self.w2_g = Variable(self.w2)
        self.b_g = Variable(self.b)

        z=self.x1_g*self.w1_g+self.x2_g*self.w2_g + self.b_g

        #gradient sigmoid
        z_neg=z*neg
        z_sig= sig_value1 / (sig_value1 + z_neg.exp())

        return z_sig


    #calcul de l'erreur avec les variables
    def erreur(self,z_sig,i):
        pui=Variable(2)
        cible_object=Variable(liste_cible_max[i])
        e = (cible_object - z_sig)**pui
        return e


    #derive partiel avec E
    def apprentissage(self):
        E=0
        y_learn_liste=[]
        global compt
        #print("Estimations learn class")
        # boucle pour x1 et x2
        for i in range(n2):
            
            x1=liste_data[i][0]
            x2=liste_data[i][1]
            self.x1_g = Variable(x1)
            self.x2_g = Variable(x2)
            z_sig = self.prediction(x1,x2)
            e = self.erreur(z_sig,i)

            if compt % 10 == 0:
                self.w1,self.w2,self.b=self.derive_partiel(e)
                
            #recalcul des valeurs pour listage et modélisation
            z=x1*self.w1+x2*self.w2+self.b
            z=sigmoid(z)
            
            
            if z >0.5:
                y_learn_liste.append(1)
            else:
                y_learn_liste.append(0)
            
            #calcul somme des erreurs
            E+=e.value
            compt+=1
        return E


    def derive_partiel(self,e):
        #nouvelle méthode
        # dérivées partielles
        de_dw1=calcul_gradient(e,self.w1_g)
        de_dw2=calcul_gradient(e,self.w2_g)
        de_db=calcul_gradient(e,self.b_g)
        
         # maj des valeurs avec les gradients
        self.w1 = self.w1-learning_rate*de_dw1
        self.w2 = self.w2-learning_rate*de_dw2
        self.b = self.b-learning_rate*de_db
        
        return(self.w1,self.w2,self.b)
        
    
    #analyse de l'apprentissage avec un nouveau E et nouvelles datas
    def analyse(self):
        E_analyse=0
        y_liste=[]
        n2=len(liste_data_analyse)

        for x in range(n2):
            x1=liste_data_analyse[x][0]
            x2=liste_data_analyse[x][1]

            z=x1*self.w1+x2*self.w2+self.b

            z=sigmoid(z)

            #calcul erreur de l'analyse
            e = (z - liste_cible_max_analyse[x])**2

            if z >=0.5:
                y_liste.append(1)
            else:
                y_liste.append(0)

            E_analyse+=e

        #Evaluation de la précision du modèle et de s'adapter à de nouvelles données
        print("Accuracy Score analyse :", accuracy_score(liste_cible_max_analyse,y_liste))
        #print(liste_cible_max_analyse)
        #print(y_liste)
        return E_analyse


    def exec(self):
        liste_E=[]
        for i in tqdm(range(EPOCHS)):
            learn=self.apprentissage()
            liste_E.append(learn)
        return liste_E


if __name__=="__main__":
    neurore=Neurone()
    liste_E=neurore.exec()
    analyse=neurore.analyse()
    print("E de l'analyse :",analyse)
    x_points=np.linspace(0,EPOCHS,EPOCHS)
    plt.plot(x_points,liste_E)
    plt.ylabel('erreurs')
    plt.title('Evolution de l\'erreur E '
    'en fonction des EPOCHS')
    plt.show()