
array = []
n = 2
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
while len(array) <= 10001:
    if checkForPrime(n) == True:
        array.append(n)
        print(len(array), ':', n)
        n += 1
    else:
        n += 1
print(array[10001])
