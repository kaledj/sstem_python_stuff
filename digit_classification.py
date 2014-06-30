import pylab as pl 
import numpy as np
from sklearn import datasets


##
##	SCOTT WRITE HELPER FUNCTIONS PLS TYHNANZ
##
def distance(x, y):
	return 1
## THANKS SCOTT


# Load the digits dataset
digits = datasets.load_digits()
print(digits.images)

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
	print image
	print distance(1, 5)

# Use classification to compute m(t+1) 

# Update t = t + 1

# Check for convergence ||m(t) - m(t-1)|| < convergence threshold

if __name__ == '__main__':
	main()