def aléatoire():
     x1=0
     x2=0
     l=[]
     for i in range(100):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        l.append(x)
        l.append(y)
     return l
print(aléatoire())