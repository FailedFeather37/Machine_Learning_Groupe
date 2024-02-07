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
            x2=liste_data[i:i+1]
            x2=x2[0]
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

            #print(self.w1,self.w2,self.b,e)
        
        return E 



if __name__=="__main__":
    neurore=Neurone()
    #a=neurore.prediction(liste_data[0],liste_data[1])
    liste_E=[]
    for i in range(10000):
        a=neurore.apprentissage()
        liste_E.append(a)
        
    x_points=np.linspace(0,10000,10000)
    plt.plot(x_points,liste_E)
    plt.ylabel('erreurs')
    plt.title('Evolution de l\'erreur E des '
    'estimations en fonction du nombre d\'estimations')
    plt.show()


"""

faire analyse

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

((x1,x2),y1) --> y1^

1. __init__ avec les poids (class)
2. calcul prediction selon x1 et x2 (class)
3. calcul de l'erreur avec les variables  ( dans main)
4. apprentissage avec E (class)
"""


""" prediction
for i in range(EPOCHS):

    # boucle qui pour x1 et x2
    x1=liste_data[i]
    x2=liste_data[i:i+1]
    x2=x2[0]

    x1_g = Variable(x1)
    x2_g = Variable(x2)
    w1_g = Variable (w1)
    w2_g = Variable (w2)
    b_g = Variable(b)

    z=x1_g*w1_g+x2_g*w2_g + b_g

    z_neg=z*neg
    #gradient sigmoid
    z_sig= sig_value1 / (sig_value1 + z_neg.exp())
"""

""" erreur
    cible_object=Variable(liste_max_cible[i])
    #gradient erreur
    e = (cible_object - z_sig)**pui
"""

""" apprentissage
    # dérivées partielles
    de_dw1=calcul_gradient(e,w1_g)
    de_dw2=calcul_gradient(e,w2_g)
    de_db=calcul_gradient(e,b_g)
    de_dx1=calcul_gradient(e,x1_g)
    de_dx2=calcul_gradient(e,x2_g)

    # maj des valeurs avec les gradients
    w1 = w1-learning_rate*de_dw1
    w2 = w2-learning_rate*de_dw2
    b = b-learning_rate*de_db
"""

""" optionnel
    #recalcul des valeurs pour listage et modélisation
    z=x1*w1+x2*w1+b
    z=sigmoid(z)

    #recalcul valeur erreur (y1' - y1)**2
    e = (z - liste_max_cible[i])**2
"""