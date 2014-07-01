#1
x = y = z = 0
for x in range(0, 9):
	for y in range(0, 9):
		for z in range(0, 9):
			equal = (100*x+10*y+z) == (81*z+9*y+x)
			if equal:
				print x, y, z


# 4

# count = 0
# for i in range(1, 6):
# 	for j in range(1, 6):
# 		for k in range(1, 6):
# 			if (i*j*k) % 2 == 1:
# 				count += 1
# print count