import time
s_t = time.time()
gg = {}
pol = []
def findBiggest(list):
	biggest = list[0]
	biggest_index = 0
	for i in range(1, len(list)):
		if list[i] > biggest:
			biggest = list[i]
			biggest_index = i
		return biggest
def checkForPol(num):
	RevNum = num[::-1]
	if RevNum == num:
		return True
	else:
		return False
for i in range(1000000, 10000, -1):
	if checkForPol(str(i)) == True:
		for j in range(100,1000):
			if i%j == 0 and len(str(i//j)) == 3:
				gg.update({i:j})
				pol.append(i)
			else:
				pass
	else:
		pass

print('The biggest polindrom is {0} and number is {1}'.format(findBiggest(pol), gg[findBiggest(pol)]))
print(time.time()-s_t, 's')
