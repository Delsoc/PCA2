import Init
import random
import numpy as np
import numpy.matlib
#import eforrlsa
from copy import deepcopy
#c = np.matlib.repmat(5, 3,1)
#print(np.dot(c.T,c))

'''pm = Parameter.Parameter()
print(pm.criterion)
print(pm.shape[0])
init.initialize()
print(pm.rows)
print(pm.columns)
print(pm.log_precomp)

parameters,units = Init.initialize()
print(parameters.shape[0])
b=parameters.shape[0]*2
print(b)
#a = [[0.020751949359402,0.953393346194937],[0.633648234926275,0.003948266327914],[0.748803882538612,0.512192263385777],[0.498507012302590,0.812620961652114],[0.224796645530848,0.612526066829388],[0.198062864759624,0.721755317431800],[0.760530712198959,0.291876068170633],[0.169110836562535,0.917774122512943],[0.088339814174010,0.714575783397691],[0.685359818367797,0.542544368011261]]
u, s, vh = np.linalg.svd(np.random.rand(10,2), full_matrices=False)
#h, tau = np.linalg.qr(a)
out_mat = np.matlib.repmat(7, 2, 2)
print(out_mat)

parameters,units = Init.initialize()
EditUnits = eforrlsa.eforrlsa(units)
print(EditUnits.Dt)
for i in range(0,2):
    print(i)
    
a=2
if a==2:
    print("right")
else:
    print("wrong")
if a==22:
    print("c")
EFO_p  = np.zeros((2, 1))
print(EFO_p)
print(EFO_p[1]*EFO_p[1])

parameters,units = Init.initialize()
a=units.y[0]
print(a)
parameters,units = Init.initialize()
print(units.weight)
print(units.weight[0][0])
#for i in range(0,len(units.weight)):
   # units.weight[i][1]=2
print(units.weight)
print("neuer Test:")
units.weight[...,1]=2
print(units.weight)
c=units.weight[...,1]
print(c)

for i in range(0,6):
    print("i: ",i)
    for j in range(0,i+1):
        print(j)
a = [1, 1, 4.5, 3, 2, 2+1j]
b = np.isreal(a)

real=0
for k in range(0,len(b)):
    if b[k]==False:
        real=1
print(real)
a=-1
print(abs(a))

parameters,units = Init.initialize()
units.eigenvalue[0] = 400
print(units.eigenvalue)
units.eigenvalue[:] = units.eigenvalue[::-1]
print(units.eigenvalue)

print(sum(units.eigenvalue))

editUnits = deepcopy(units)
parameters,units = Init.initialize()

print(units.mt)
units.mt[0] = 43
units.mt[1] = -26
units.mt = units.mt/2
units.mt = abs(units.mt)
minimum = min(units.mt)
print(units.mt)
print(minimum)

# alphabets list

import test2

alphabets = [1,2,3,4,5,6,7,8,8]

test2.test1(alphabets)

print(alphabets)
testarray = np.zeros((10, 1))
testarray += 5
transponiert = testarray.T
Produkt =  transponiert * testarray
Produkt2 = testarray * transponiert
for i in range(1000):
    a=random.uniform(0.1, 1.0)
    print(a)
a = np.random.rand(10, 1)
print(a)
print("b:")
b= np.hstack((a,a))
print(b)
print('%s %d' % ("namen: ",1))
a = np.random.rand(3, 1)
print(a)
print(sum(a))
print("b")
b= a[:len(a)-1]
print(b)
a = np.arange(12).reshape(3, 4)
print(a)
b = np.delete(a,len(a),1)
print(b)

a = np.zeros((3, 1))
print(a)
b= a.T
print(b)
print(4)'''
#ERG = array.flatten()
x = np.array([1, 2])
y = np.array([0.7715, -0.0530])
z= np.polyfit(x, y, 1)
print(z)









