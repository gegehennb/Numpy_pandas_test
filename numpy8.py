import numpy as np 

a=np.arange(4)
# print(a)

b=a
c=a
d=b

a[0]=11

print(a)

# d[1:3]=[22,33]

# print(d)
# print(a)

b=a.copy()

b[0]=22

print(b)
