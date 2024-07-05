from init_data_matrice import *
from deriv import *
from math import *
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, accuracy_score
import numpy as np



learning_rate=0.01
EPOCHS=200
compt=0

class Neurone:
    def __init__(self):
        self.w1=W[0]
        self.w2=W[1]
        self.b=b
    
    def prediction(self,x1,x2):
        neg=Variable(-1)
        sig_value1=Variable(1)
        self.x1_g = Variable(x1)
        self.x2_g = Variable(x2)
        self.w1_g = Variable(self.w1)
        self.w2_g = Variable(self.w2)
        self.b_g = Variable(self.b)
        z=self.x1_g*self.w1_g+self.x2_g*self.w2_g + self.b_g
        #Gradient sigmoid
        z_neg=z*neg
        z_sig= sig_value1 / (sig_value1 + z_neg.exp())
        return z_sig

    #Calcul de l'erreur avec les variables
    def erreur(self,z_sig,i):
        pui=Variable(2)
        cible_object=Variable(L[i])
        e = (cible_object - z_sig)**pui
        return e


    def apprentissage(self):
        E=0
        y_learn_liste=[]
        global compt
        #Boucle pour x1 et x2
        for i in range(len(X)):
            x1=X[i][0]
            x2=X[i][1]
            self.x1_g = Variable(x1)
            self.x2_g = Variable(x2)
            z_sig = self.prediction(x1,x2)
            e = self.erreur(z_sig,i)

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
        print("Predi :",y_learn_liste)
        print("L : ",L )
        print("Accuracy Score apprentissage :", accuracy_score(L,y_learn_liste))
        return E
    
    def derive_partiel(self,e):
        de_dw1=calcul_gradient(e,self.w1_g)
        de_dw2=calcul_gradient(e,self.w2_g)
        de_db=calcul_gradient(e,self.b_g)
        
        # maj des valeurs avec les gradients
        self.w1 = self.w1-learning_rate*de_dw1
        self.w2 = self.w2-learning_rate*de_dw2
        self.b = self.b-learning_rate*de_db
        
        return(self.w1,self.w2,self.b)
    

    def analyse(self):
        E_analyse=0
        y_liste=[]
        for i in range(len(X_analyse)):
            x1=X_analyse[i][0]
            x2=X_analyse[i][1]
            z=x1*self.w1+x2*self.w2+self.b
            z=sigmoid(z)

             #calcul erreur de l'analyse
            e = (z - L_analyse[i])**2
            
            if z >0.5:
                y_liste.append(1)
            else:
                y_liste.append(0)

            E_analyse+=e


        print(X_analyse)
        print("Predi_analyse :",y_liste)
        print("L_analyse : ",L_analyse )

        fpr, tpr, _ = roc_curve(L_analyse, y_liste)

        # Tracer la courbe ROC
        plt.figure()
        plt.plot(fpr, tpr)
        plt.title("Courbe ROC")
        plt.show()
        return E_analyse


    def exec(self):
        liste_E=[]
        for _ in (range(EPOCHS)):
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
    
