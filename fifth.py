import math

def Calc(num):
	ans = 1
	for i in range(1, num + 1):
		ans *= i//math.gcd(i, ans)
	return str(ans)

if __name__ == "__main__":
	print(Calc(20))
