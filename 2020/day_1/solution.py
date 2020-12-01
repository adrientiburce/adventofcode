input = open('input.txt', 'r') 
lines = input.readlines() 
  
count = 0
numbers = []
for line in lines: 
	try:
		numbers.append(int(line.rstrip()))
	except:
		print("not a number")
	count += 1

for i in range(len(numbers)):
	for j in range(i+1, len(numbers)):
		n1, n2 = numbers[i], numbers[j]
		if n1 + n2 == 2020:
			print(f" {n1} + {n2} = 2020 >> {n1*n2}")
			i = len(numbers)
			break
			

for i in range(len(numbers)):
	for j in range(i+1, len(numbers)):
		for k in range(j+1, len(numbers)):
			n1, n2, n3 = numbers[i], numbers[j], numbers[k]
			if n1 + n2 + n3 == 2020:
				print(f" {n1} + {n2} + {n3} = 2020 >> {n1*n2*n3}")
				exit()

