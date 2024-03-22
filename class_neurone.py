from calendar import EPOCH
from init_data import *
from deriv import *
from math import *
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np
from tqdm import tqdm


learning_rate=0.2
liste_learn=[]
EPOCHS=200
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
        # boucle pour x1 et x2
        for i in range(len(liste_data)):
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
        #print("Accuracy Score apprentissage :", accuracy_score(liste_cible_max,y_learn_liste))
        return E


    def derive_partiel(self,e):
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

        for x in range(len(liste_data_analyse)):
            x1=liste_data_analyse[x][0]
            x2=liste_data_analyse[x][1]

            z=x1*self.w1+x2*self.w2+self.b

            z=sigmoid(z)

            #calcul erreur de l'analyse
            e = (z - liste_cible_max_analyse[x])**2
            
            if z >0.5:
                y_liste.append(1)
            else:
                y_liste.append(0)

            E_analyse+=e

        #Evaluation de la précision du modèle et de s'adapter à de nouvelles données
        VP,VN,FP,FN,liste_tvp,liste_tfp = eval(liste_cible_max_analyse,y_liste)
        
        accuracy=(VP+VN)/(VP+VN+FP+FN)
        print("Accuracy Score analyse :", accuracy)
        
        precision=VP/(VP+FP)
        print("Precision analyse :", precision)
        
        rappel=VP/(VP+FN)
        print("Rappel analyse :", rappel)
        
        f_score=2/((1/precision)+(1/rappel))
        print("f score analyse :", f_score)
        
        plt.plot(liste_tvp,liste_tfp)
        plt.show()
        
        return E_analyse

    
    def exec(self):
        liste_E=[]
        for i in (range(EPOCHS)):
            learn=self.apprentissage()
            liste_E.append(learn)
        return liste_E


def eval(liste_cible_max_analyse,y_liste):
    VP=0
    VN=0
    FP=0
    FN=0
    liste_tvp=[]
    liste_tfp=[]
    tvp=0
    tfp=0
    for i in range(len(liste_cible_max_analyse)):
        
        if liste_cible_max_analyse[i]==1 and y_liste[i]==1:
            VP+=1
        elif liste_cible_max_analyse[i]==0 and y_liste[i]==0:
            VN+=1
        elif liste_cible_max_analyse[i]==0 and y_liste[i]==1:
            FP+=1
        elif liste_cible_max_analyse[i]==1 and y_liste[i]==0:
            FN+=1
        tvp= VP/len(liste_cible_max_analyse)
        tfp = FP/len(liste_cible_max_analyse)
        liste_tvp.append(tvp)
        liste_tfp.append(tfp)
    return VP,VN,FP,FN,liste_tvp,liste_tfp
    
    
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
    
