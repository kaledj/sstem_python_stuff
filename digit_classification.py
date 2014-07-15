import pylab as pl
import numpy as np
import cProfile, pstats, StringIO
from sklearn import datasets
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from numpy import random


# #
# #	SCOTT WRITE HELPER FUNCTIONS PLS THANKS
# #
pr = cProfile.Profile()
pr.enable()
def distanceAndClassify(y):
    dis = np.zeros(10)
    for z in range(10):
     #   for q in range(64):
      #      d1 = (m[z][q] - y[q]) ** 2
       #     dis[z] += d1
        #dis[z] = np.sqrt(dis[z])
        dis[z] = np.sqrt(np.sum((m[z] - y) ** 2))
    return np.argmin(dis)
   

def score(clusterlist):
    images = np.zeros((len(digits.images), 64))
    labels = np.zeros((len(digits.images)))
    count = 0
    for x in clusterlist:
        for x0, x1 in zip(x[0], x[1]):
            images[count] = x0
            labels[count] = x1
            count += 1
    estimate = KMeans(init='random', n_clusters=10)
    estimator = estimate.fit(digits.data)
    print ('Adj. Mutual Info Score: %.3f' % (metrics.adjusted_mutual_info_score(digits.target, labels)))
    print ('Norm Mutual Info Score: %.3f' % (metrics.normalized_mutual_info_score(digits.target, labels)))
    print ('Adj. Rand Score: %.3f' % (metrics.adjusted_rand_score(digits.target, labels)))
    print ('Silhouette Score: %.3f' % (metrics.silhouette_score(images, labels, metric='euclidean')))
    pca = PCA(n_components=len(images))
    pca.fit(images)

    print (pca.explained_variance_ratio_)
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
#pl.show()

converged = False
attemptnum = 0
numlist = []
while not converged:
    # Initialize classification lists for current step
    numlist = []
    for i in range(0, 10):
        numlist.append(([], []))
    print "Attempt: %d" % attemptnum

    # Classify input data according to m(t=0)
    for index, image in enumerate(digits.images):
        closest = distanceAndClassify(image.flatten())
        numlist[closest][0].append(image.flatten())
        numlist[closest][1].append(digits.target[index])

    # Recomputed the vector of means
    mlast = m.copy()
    for i in range(10):
        if len(numlist[i][0]) > 0:
            m[i].put(range(64), np.average(numlist[i][0], axis=0).astype(np.dtype(np.int32)))
    attemptnum += 1
    if np.any(m - mlast) == 0:
        converged = True

for i in range(10):
    pl.subplot(2, 5, i + 1)
    pl.imshow(m[i].reshape((8, 8)), cmap=pl.cm.gray_r, interpolation='nearest')
    #pl.imshow(digits.images[i], cmap=pl.cm.gray_r, interpolation='nearest')
pl.show()

score(numlist)

pr.disable()
string = StringIO.StringIO()
ps = pstats.Stats(pr, stream=string).sort_stats('time')
ps.print_stats()
print string.getvalue()