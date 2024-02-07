from init_data import *
from math import *
import matplotlib.pyplot as plt
import numpy as np


class Variable:
    def __init__(self, value,gradient=()):
        self.value = value
        self.gradient=gradient


    def __add__(self, other):
        addi=self.value + other.value
        gradient=[(self,1),(other,1)]
        c = Variable(addi,gradient)
        return c

    def __sub__(self, other):
        sub =self.value - other.value
        gradient=[(self,1),(other,-1)]
        d = Variable(sub,gradient)
        return d

    def __mul__(self, other):
        mul=self.value * other.value
        gradient=[(self,other.value),(other,self.value)]
        e = Variable(mul,gradient)
        return e

    def __truediv__(self, other):
        truediv=self * other.inv()
        return truediv

    def __pow__(self,other):
        pow=self.value ** other.value
        gradient=[(self,other.value*self.value**(other.value-1))]
        g = Variable(pow,gradient)
        return g

    def inv(self):
        inv=1/self.value
        gradient=[(self,(-1/(self.value)**2))]
        f = Variable(inv,gradient)
        return f

    def exp(self):
        exp_value=exp(self.value)
        gradient=[(self,exp(self.value))]
        h = Variable(exp_value,gradient)
        return h




def calcul_gradient(variable,rapport):
    gradient = 0
    for enfant in variable.gradient:
        if enfant[0] == rapport:
            gradient += enfant[1]
        else:
            recur=calcul_gradient(enfant[0],rapport)
            gradient += recur * enfant[1]
    return(gradient)



n2=int(n/2)
learning_rate=0.4
liste_learn=[]
EPOCHS=n2
if __name__=="__main__":

    
    liste_machine_learn=[]
    
    
    
    z=f_complexe(somme)
    w1=liste_poids[0]
    w2=liste_poids[1]
    b=1
    neg=Variable(-1)
    sig_value1=Variable(1)
    pui=Variable(2)


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

        cible_object=Variable(liste_max_cible[i])
    #gradient erreur
        e = (cible_object - z_sig)**pui

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

    #recalcul des valeurs pour listage et modélisation
        z=x1*w1+x2*w2+b
        z=sigmoid(z)

    #recalcul valeur erreur (y1' - y1)**2
        e = (z - liste_max_cible[i])**2
        liste_learn.append(e)

        #print(w1,w2,b,e)
    #print(liste_learn)


    E=0
    for i in liste_learn:
        E+=i
#print(E)

"""
#x_point=np.linspace(0,1,n2)
y_point=liste_learn
plt.plot(y_point)
plt.ylabel('erreurs')
plt.title('Evolution de l\'erreur des '
'estimations en fonction du nombre d\'estimations')
plt.show()
"""

