from init_data import *
from deriv import *
from math import *


class Neurone:
    def __init__(self): #1
        self.w1=liste_poids[0]
        self.w2=liste_poids[1]
        self.b=b

    def prediction(self,x1,x2): #2 calcul prediction selon x1 et x2 (class)
        neg=Variable(-1)
        neg=Variable(-1)
        sig_value1=Variable(1)


        self.x1_g = Variable(x1)
        self.x2_g = Variable(x2)
        self.w1_g = Variable (self.w1)
        self.w2_g = Variable (self.w2)
        self.b_g = Variable(self.b)

        z=self.x1_g*self.w1_g+self.x2_g*self.w2_g + self.b_g

        z_neg=z*neg
        #gradient sigmoid
        z_sig= sig_value1 / (sig_value1 + z_neg.exp())

        return z_sig

    def erreur(self,z_sig,i): #3 calcul de l'erreur avec les variables
        pui=Variable(2)
        cible_object=Variable(liste_max_cible[i])
        #gradient erreur
        e = (cible_object - z_sig)**pui
        return e


    def apprentissage(self): #derive partiel avec E
        E=0
        #print("Estimations class")
        for i in range(n2):
            x1=liste_data[i]
            x2=liste_data[i+1]
            self.x1_g = Variable(x1)
            self.x2_g = Variable(x2)
            z_sig=self.prediction(x1,x2)
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

            #nouvelle méthode
            z=x1*self.w1+x2*self.w2+b
            z=sigmoid(z)

            e = (z - liste_max_cible[i])**2
            E+=e

            print(self.w1,self.w2,self.b,e)

        return E

    def analyse(self):
        E=0
        for i in range(1):
        #print("Estimations class")
            x1=liste_data[i]
            x2=liste_data[i+1]


        #nouvelle méthode
            z=x1*self.w1+x2*self.w2+b
            z=sigmoid(z)
            print(liste_max_cible[i],x1,x2,b,z)
            e = (z - liste_max_cible[i])**2


        return e,z



if __name__=="__main__":
    neurore=Neurone()
    a=neurore.analyse()
    print(a)