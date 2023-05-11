results = {}
for i in range(1, 1000001):
    num = i
    startNumber = i
    numberOfOperations = 0
    print(num)
    while num != 1:
        if num % 2 == 0:
            num /= 2
            numberOfOperations += 1
        else:
            num = 3 * num + 1
            numberOfOperations += 1
    results[numberOfOperations] = startNumber
print(results[max(results)])