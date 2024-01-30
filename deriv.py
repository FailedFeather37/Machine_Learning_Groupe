from init_data import *
from math import *

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

if __name__=="__main__":
    a = Variable(5)
    b = Variable(6)

    c = a + b
    print("c :",c.value,c.gradiant)
    d = a - b

    e = a * b
    print("e :",e.value)
    f = a / b

    print("f :",f.value)

    h=a.exp()

    print("h :",h.value)

    z=f_complexe()
    liste_poids=poids()
    liste_data=data_set()
    x1=liste_data[0]
    x2=liste_data[0]
    w1=liste_poids[0]
    w2=liste_poids[1]
    b=1
    
    z= Variable(z)
    x1 = Variable(x1)
    x2 = Variable(x2)
    w1 = Variable (w1)
    w2 = Variable (w2)
    b = Variable(b)
    z=x1*w1
    
    
    
    sigmoid = z.exp()
    print(sigmoid.gradiant)
    
    
    



"""
sigmoid = 1/ 1 + exp(-x)

"""
