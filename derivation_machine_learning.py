class variable:

    def __valeur__(self):
        a=a
        b=b
        c=a.valeur+b.valeur
    def __derivees_locals__():
    def __add__():
    def __sub__():
    def __nul__():
        inv()
    def __truediv__
partie chatgpt de merde
class Variable:
    def __init__(self, valeur):
        self.valeur = valeur

    def __add__(self, other):
        if isinstance(other, Variable):
            return Variable(self.valeur + other.valeur)
        else:
            raise TypeError("Unsupported operand type for +: {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Variable):
            return Variable(self.valeur - other.valeur)
        else:
            raise TypeError("Unsupported operand type for -: {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, Variable):
            return Variable(self.valeur * other.valeur)
        else:
            raise TypeError("Unsupported operand type for *: {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, Variable):
            if other.valeur != 0:
                return Variable(self.valeur / other.valeur)
            else:
                raise ValueError("Division by zero")
        else:
            raise TypeError("Unsupported operand type for /: {}".format(type(other)))

    def __str__(self):
        return str(self.valeur)

# Example usage:
a = Variable(5)
b = Variable(3)

c = a + b
print(c)  # Output: 8

d = a - b
print(d)  # Output: 2

e = a * b
print(e)  # Output: 15

f = a / b
print(f)  # Output: 1.6666666666666667
