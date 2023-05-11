def calc(num):
	sum1 = 0
	sum2 = 0
	for i in range(1, num + 1):
		sum1 += i ** 2
	for j in range(1, num+1):
		sum2 += j
	return sum2**2-sum1

if __name__ == '__main__':
	print(calc(100))
