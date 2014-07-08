import pylab as pl
import numpy as np
from sklearn import datasets
from numpy import random


# #
# #	SCOTT WRITE HELPER FUNCTIONS PLS THANKS
##
def distanceAndClassify(y):
    dis = np.zeros(10)
    for z in range(10):
        for q in range(64):
            d1 = (m[z][q] - y[q]) ** 2
            dis[z] += d1
        dis[z] = np.sqrt(dis[z])
    return np.argmin(dis)

## THANKS SCOTT
## WELCOME KALE

# Load the digits data set
digits = datasets.load_digits()
#print(digits.images)

'''
 K-Means clustering
'''


# Randomly initialize solution as vectors of means m(t=0)=[m1...mk] 
m = np.empty((10, 64))
mlast = np.empty((10, 64))
for i in range(0, 10):
    #m[i] = np.random.random_integers(0, 16, 64)
    rand_sample = random.randint(0, len(digits.images))
    m[i] = digits.images[rand_sample].flatten()

for i in range(10):
    pl.subplot(2, 5, i + 1)
    pl.imshow(m[i].reshape((8, 8)), cmap=pl.cm.gray_r, interpolation='nearest')
    #pl.imshow(digits.images[i], cmap=pl.cm.gray_r, interpolation='nearest')
pl.show()


converged = False
attemptnum = 0
while not converged:
    # Initialize classification lists for current step
    numlist = []
    for i in range(0, 10):
        numlist.append([])
    print "Attempt : %d" % attemptnum
    print numlist

    # Classify input data according to m(t=0)
    for image in digits.images:
        closest = distanceAndClassify(image.flatten())
        numlist[closest].append(image.flatten())

    # Recomputed the vector of means
    mlast = m.copy()
    for i in range(10):
        if len(numlist[i]) > 0:
            print len(numlist[i])
            m[i].put(range(64), np.average(numlist[i], axis=0).astype(np.dtype(np.int32)))
            print type(m[i])
    print "Attempt: %d" % attemptnum
    attemptnum += 1
    if np.any(m - mlast) == 0:
        converged = True

for i in range(10):
    pl.subplot(2, 5, i + 1)
    pl.imshow(m[i].reshape((8, 8)), cmap=pl.cm.gray_r, interpolation='nearest')
    #pl.imshow(digits.images[i], cmap=pl.cm.gray_r, interpolation='nearest')
pl.show()