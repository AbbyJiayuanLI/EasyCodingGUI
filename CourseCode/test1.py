# -*- coding: utf-8 -*-

# 1 import numpy library
import ___

# 2 input training sample eigenvector
X = np.array___

# 3 input training sample tag
Y_label = np.array___

# given initial weight 
W =np.array([0,0,0])

# given learning rate
learning_rate = 0.01

# 4 define loss function
def loss_function(Y_label, Y):
    ___

# 5,6 define training function       
def training(learning_rate,Y_label,X,W):
    Y=np.___
    n=loss_function(Y_label, Y)

    while(n!=0):
        n=loss_function(Y_label, Y)
        delta_W = learning_rate*___ 
        W = W + delta_W
        Y=np.sign(np.dot(X,W))
    return W

# training, and return the result to w
W=training(learning_rate,Y_label,X,W)
print(W)