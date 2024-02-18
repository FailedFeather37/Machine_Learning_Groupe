from math import *


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