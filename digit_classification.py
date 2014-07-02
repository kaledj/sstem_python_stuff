import pylab as pl
import numpy as np
from sklearn import datasets


# #
##	SCOTT WRITE HELPER FUNCTIONS PLS THANKS
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
## WELCOME KALE

# Load the digits data set
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
mlast = np.empty((10, 64))
for i in range(0, 10):
    m[i] = np.random.random_integers(0, 16, 64)
#print(m[0:])

converged = False
attemptnum = 0
while not converged:
    # Classify input data according to m(t=0)
    for image in digits.images:
        distanceAndClassify(image.flatten())

    # Recomputed the vector of means
    for i in range(10):
        mlast[i] = m[i]
        if len(numlist[i]) > 0:
            m[i] = (np.average(numlist[i], axis=0).astype(np.dtype(np.int16)))
    print "Attempt: %d" % attemptnum
    attemptnum += 1
    if np.any(abs(m - mlast)) == 0:
        converged = True
        print (abs(m - mlast))

for i in range(10):
    pl.subplot(2, 5, i + 1)
    pl.imshow(m[i].reshape((8, 8)), cmap=pl.cm.gray_r, interpolation='nearest')
pl.show()