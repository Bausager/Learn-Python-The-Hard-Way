numbers = []


def list(x):
	for i in range(1, x):
		
		print(f"At the top i is {i}")
		numbers.append(i)


		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")



list(3)


print("The numbers: ")

for num in numbers:
	print(num)
