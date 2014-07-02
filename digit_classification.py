import pylab as pl
import numpy as np
from sklearn import datasets


# #
##	SCOTT WRITE HELPER FUNCTIONS PLS TYHNANZ
##
def distanceAndClassify(y):
    dis = np.zeros(10)
    for z in range(0, 10):
        for q in range(0, 64):
            d1 = int(np.absolute(m[z][q] - y[q])) ^ 2
            dis[z] += d1
        dis[z] = np.sqrt(dis[z])
    lowest = np.argmin(dis)
    numlist[lowest].append(y)

## THANKS SCOTT


# Load the digits dataset
digits = datasets.load_digits()
print(digits.images)

numlist = []
for nl in range(0, 10):
    numlist.append([])

'''
 K-Means clustering
'''


# Randomly initialize solution as vectors of means m(t=0)=[m1...mk] 
m = np.empty((10, 64))
for i in range(0, 10):
    m[i] = np.random.random_integers(0, 16, 64)
#print(m[0:])

# Classify input data according to m(t=0)
for image in digits.images:
    distanceAndClassify(image.flatten())

for l in numlist:
    print len(l)


#print image
#print distance(1, 5)

# Use classification to compute m(t+1) 

# Update t = t + 1

# Check for convergence ||m(t) - m(t-1)|| < convergence threshold