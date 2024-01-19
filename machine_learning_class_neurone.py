
def gradients(A,X,y):
    dW=1/len(y)*np.dot(X.T, A-y)
    db=1/len(y)*np.sum(A-y)

dW,db(X,y,A)
dW.shape
class neurone(X,y,learning_rate=0.1,nombre_iter=100,):
    __init__()
    poid1=randint(1,10)
    poid2=randint(1,10)
    poid3=randint(1,10)

    W,B=init(X)

    for i in range(nombre_iter):
        A=model(X,W,B)
        Loss=log_loss(A,y)
        dW, db=gradients