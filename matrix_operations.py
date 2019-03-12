'''' Python Program for matrix product '''


import numpy as np
a= np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)    #shows the array index
b=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(b.shape)
c=np.matmul(a,b)  #matrix product
print("product=\n",c)
