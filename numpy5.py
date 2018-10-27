import numpy as np 

A=np.arange(3,15).reshape((3,4))
print(A)

# print(A[2][1])

# print(A[1,1:3])

# print(A.T)

print(A.flatten())
for item in A.flat:
    print(item)