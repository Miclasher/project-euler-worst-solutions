def findDivs(num):
	divs = []
	for i in range(1, (num // 2 + 1)):
		if num % i == 0:
			divs.append(i)
		else:
			pass
	divs.append(num)
	return divs

def computeTriangles():
	numOfTr = 1
	tr = 0
	nOD = len(findDivs(tr))
	while nOD <= 500:
		print(tr)
		nOD = []
		tr += numOfTr
		numOfTr += 1
		nOD = len(findDivs(tr))
	return tr
print(computeTriangles())
		
