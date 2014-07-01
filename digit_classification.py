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
		numlist[0].append(y)
	elif lowest == 1:
		numlist[1].append(y)
	elif lowest == 2:
		numlist[2].append(y)
	elif lowest == 3:
		numlist[3].append(y)
	elif lowest == 4:
		numlist[4].append(y)
	elif lowest == 5:
		numlist[5].append(y)
	elif lowest == 6:
		numlist[6].append(y)
	elif lowest == 7:
		numlist[7].append(y)
	elif lowest == 8:
		numlist[8].append(y)
	else:
		numlist[9].append(y)
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

print len(numlist[0])
print len(numlist[1])
print len(numlist[2])
print len(numlist[3])
print len(numlist[4])
print len(numlist[5])
print len(numlist[6])
print len(numlist[7])
print len(numlist[8])
print len(numlist[9])


	
 

	#print image
	#print distance(1, 5)

# Use classification to compute m(t+1) 

# Update t = t + 1

# Check for convergence ||m(t) - m(t-1)|| < convergence threshold

if __name__ == '__main__':
	main()

