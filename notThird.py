#600851475143 biggest prime
array = []
def findBiggest(list):
    biggest = list[0]
    biggest_index = 0
    for i in range(1, len(list)):
        if list[i] > biggest:
            biggest = list[i]
            biggest_index = i
        return biggest_index

def checkForPrime(num):
    if num > 1:
        for i in range(2, num//2+1):
            if num%i == 0 and i != num:
                return False
            else:
                return True

if __name__ == '__main__':
    for i in range(13195, 1, -1):
        if checkForPrime(i) == True and 13195%i == 0:
            print(i)
        else:
            pass

