from machine_learning import *


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


a = Variable(5)
b = Variable(6)

c = a + b
#print(c.gradiant)
d = a - b

e = a * b
print()
f = a / b
print(f.value)