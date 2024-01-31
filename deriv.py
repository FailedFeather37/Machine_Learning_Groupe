from init_data import *
from math import *






learning_rate=0.1

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
        g= Variable(pow,gradiant)
        return g

    def inv(self):
        inv=1/self.value
        gradient=[(self,(-1/(self.value)**2))]
        f= Variable(inv,gradient)
        return f

    def exp(self):
        exp_value=exp(self.value)
        gradiant=[(self,self.value)]
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
    """
    a = Variable(3)
    b = Variable(5)
    d = a*(a+b)

    """


    z=f_complexe()
    liste_poids=poids()
    liste_data=data_set()
    x1=liste_data[0]
    x2=liste_data[0]
    w1=liste_poids[0]
    w2=liste_poids[1]
    b=1

    x1_g = Variable(x1)
    x2_g = Variable(x2)
    w1_g = Variable (w1)
    w2_g = Variable (w2)
    b_g = Variable(b)
    z=x1_g*w1_g+x2_g*w2_g + b_g
    test=Variable(1)
    z_sig= test / (test + z.exp())
    test2=Variable(z_sig,2)
    print(test2.value)


    #print(calcul_gradiant(test2,w1_g))
