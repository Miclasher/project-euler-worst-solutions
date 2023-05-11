array = [1, 2]
num = 2
sum = 0
while True:
	if array[num-2] + array[num-1] <= 4000000:
		array.append(array[num-2] + array[num-1])
		num = num+1
	else:
		break

for i in array:
	if i%2 == 0:
		sum += i
else:
	pass

print(sum)
