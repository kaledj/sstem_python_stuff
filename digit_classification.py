import pylab as pl 
import numpy as np
from sklearn import datasets


##
##	SCOTT WRITE HELPER FUNCTIONS PLS TYHNANZ
##
def distanceAndClassify(y):
	dis = np.zeros(10)
	for z in range(0,10):
		for q in range(0,64):
			d1 = int(np.absolute(m[z][q] - y[q]))^2
			dis[z] += d1
		dis[z] = np.sqrt(dis[z])
	lowest = np.argmin(dis)
	if lowest == 0:
		numlist0.append(y)
	elif lowest == 1:
		numlist1.append(y)
	elif lowest == 2:
		numlist2.append(y)
	elif lowest == 3:
		numlist3.append(y)
	elif lowest == 4:
		numlist4.append(y)
	elif lowest == 5:
		numlist5.append(y)
	elif lowest == 6:
		numlist6.append(y)
	elif lowest == 7:
		numlist7.append(y)
	elif lowest == 8:
		numlist8.append(y)
	else:
		numlist9.append(y)
## THANKS SCOTT


# Load the digits dataset
digits = datasets.load_digits()
print(digits.images)
<<<<<<< HEAD
numlist1 = []
numlist2 = []
numlist3 = []
numlist4 = []
numlist5 = []
numlist6 = []
numlist7 = []
numlist8 = []
numlist9 = []
numlist0 = []
=======

'''
 K-Means clustering
'''

>>>>>>> origin/master
# Randomly initialize solution as vectors of means m(t=0)=[m1...mk] 
m = np.empty((10, 64))
for i in range(0, 10):
	m[i] = np.random.random_integers(0, 16, 64)
#print(m[0:])

# Classify input data according to m(t=0)
for image in digits.images:
<<<<<<< HEAD
	distanceAndClassify(image.flatten())

print len(numlist0)
print len(numlist1)
print len(numlist2)
print len(numlist3)
print len(numlist4)
print len(numlist5)
print len(numlist6)
print len(numlist7)
print len(numlist8)
print len(numlist9)


	
 
=======
	print image
	print distance(1, 5)

# Use classification to compute m(t+1) 

# Update t = t + 1

# Check for convergence ||m(t) - m(t-1)|| < convergence threshold

if __name__ == '__main__':
	main()
>>>>>>> origin/master
