from init_data import *
from math import *
import matplotlib.pyplot as plt
from deriv import *
import numpy as np

class Variable:
    def __init__(self, value,gradiant=()):
        self.value = value
        self.gradiant=gradiant


    def __add__(self, other):
        addi=self.value + other.value
        gradiant=[(self,1),(other,1)]
        c = Variable(addi,gradiant)
        return c

    def __sub__(self, other):
        sub =self.value - other.value
        gradiant=[(self,1),(other,-1)]
        d = Variable(sub,gradiant)
        return d

    def __mul__(self, other):
        mul=self.value * other.value
        gradiant=[(self,other.value),(other,self.value)]
        e = Variable(mul,gradiant)
        return e

    def __truediv__(self, other):
        truediv=self * other.inv()
        return truediv

    def __pow__(self,other):
        pow=self.value ** other.value
        gradiant=[(self,other.value*self.value**(other.value-1))]
        g = Variable(pow,gradiant)
        return g

    def inv(self):
        inv=1/self.value
        gradient=[(self,(-1/(self.value)**2))]
        f = Variable(inv,gradient)
        return f

    def exp(self):
        exp_value=exp(self.value)
        gradiant=[(self,exp(self.value))]
        h = Variable(exp_value,gradiant)
        return h




def calcul_gradiant(variable,rapport):
    gradiant = 0
    for enfant in variable.gradiant:
        if enfant[0] == rapport:
            gradiant += enfant[1]
        else:
            recur=calcul_gradiant(enfant[0],rapport)
            gradiant += recur * enfant[1]
    return(gradiant)


if __name__=="__main__":
    learning_rate=0.3
    EPOCHS=20
    z=f_complexe(somme)

    # boucle qui pour x1 et x2
    x1=liste_data[0]
    x2=liste_data[1]
    w1=liste_poids[0]
    w2=liste_poids[1]
    b=1

    x1_g = Variable(x1)
    x2_g = Variable(x2)
    w1_g = Variable (w1)
    w2_g = Variable (w2)
    b_g = Variable(b)


    z=x1_g*w1_g+x2_g*w2_g + b_g
    neg=Variable(-1)
    z_neg=z*neg
    sig_value1=Variable(1)
    z_sig= sig_value1 / (sig_value1 + z_neg.exp()) #gradiant sigmoid

    pui=Variable(2)
    cible_object=Variable(liste_max_cible[0])
    e = (cible_object - z_sig)**pui #gradiant erreur
    de_dw1=calcul_gradiant(e,w1_g)
    de_dw2=calcul_gradiant(e,w2_g)
    de_db=calcul_gradiant(e,b_g)
    de_dx1=calcul_gradiant(e,x1_g)
    de_dx2=calcul_gradiant(e,x2_g)

    liste_learn=[]
    z=x1*w1+x2*w1+b
    e = (z - liste_max_cible[0])**2
    #print(liste_max_cible)

    compt=0
    liste_machine_learn=[]
    for i in range(EPOCHS):
        w1 = w1-learning_rate*de_dw1
        w2 = w2-learning_rate*de_dw2
        b = b-learning_rate*de_db

        print(w1,w2,b,e)
        z=x1*w1+x2*w1+b
        z=sigmoid(z)

        e = (z - liste_max_cible[i])**2 # (y1' - y1)**2

        liste_learn.append(e)
        machine_learn=sigmoid(x1*w1+x2*w2+b)
        liste_machine_learn.append(machine_learn)
        compt+=1
        print("estimation :",machine_learn,compt)
    print(liste_learn)

    # calcul min des erreurs
    min=liste_learn[0]
    for i in liste_learn:
        if i<min:
            min=i
    print(min)
    comptmin=0
    for i in liste_learn:
        if i==min:
            print(liste_machine_learn[comptmin])
            break
        comptmin+=1

    """
    x_point=np.linspace(0,20,20)

    y_point=liste_learn
    plt.plot(x_point,y_point)


    plt.ylabel('some numbers')
    plt.title('m')
    plt.show()
    """

"""

change valeur de x1 et x2 a chaque iteration
boucle for = E

(y1^-y1)²
(y2^-y2)²  --> E calcul gradiant
(y3^-y3)²
(y3^-y3)²

((x1,x2),y1) --> y1^

1. __init__ avec les poids (class)
2. calcul prediction selon x1 et x2 (class)
3. calcul de l'erreur avec les variables  ( dans main)
4. apprentissage avec E (class)
"""