def checkForPrime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
sum = 75286062899
for i in range(1434457, 2000001):
	if checkForPrime(i) == True:
		print(i)
		sum += i
	else:
		pass
print(sum)
		
