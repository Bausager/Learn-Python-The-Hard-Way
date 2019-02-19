import random

things_for_milk = ["Pasteurizing Heat", "Internal Travel Time", "Metal in the Milk", "Travel Time"]
milk_list = []
print("""You have to make some milk and do some decisions.
How hot does it get to pasteurize it?""")
temp = input("> ")

try:
	val = int(temp)
	milk_list.append(val)
except ValueError:
	print("Are you a total idiot? Jesus!")
	exit(0)

print("How long does it take to get to the otherside of the factory in minutes?")
temp = input("> ")

try:
	val = int(temp)
	milk_list.append(val)
except ValueError:
	print("Are you a total idiot? Jesus!")
	exit(0)

print("Does the inductive sensor pick something up? y/n?")
temp = input("> ")

if temp == "y" or temp == "Y" or temp == "n" or temp == "N":
	milk_list.append(temp)
else:
	print("Are you a total idiot? Jesus!")
	exit(0)

print("How long is the transport time in full hours?")
temp = input("> ")

try:
	val = int(temp)
	milk_list.append(val)
except ValueError:
	print("Are you a total idiot? Jesus!")
	exit(0)

print(milk_list[2])
print("Mr. and Mrs. Douchebag is complaining how the milk")

final = random.randint(0, 3)

if final == 0:
	print(f"They think it's the {things_for_milk[final]} that wasn't high enough")
	if milk_list[final] < 70:
		print(f"They might be right. The {things_for_milk[final]}: {milk_list[final]} is lower then 70. YOU JUST GOT SUED!")
		exit(0)
	else:
		print(f"YOU WIN! Since {things_for_milk[final]}: {milk_list[final]} is more then 70 degress, it's over the law requements.")
elif final == 1:
		print(f"They think it's the {things_for_milk[final]} is too long")
		if milk_list[final] > 10:
			print(f"They might be right. The {things_for_milk[final]}: {milk_list[final]} is longer then 10 minuts. YOU JUST GOT SUED!")
			exit(0)
		else:
			print(f"YOU WIN! Since {things_for_milk[final]}: {milk_list[final]} is shoter then 10 minuts, it's under the law requements.")
elif final == 2:
		print(f"They think there's {things_for_milk[final]}")
		if milk_list[final] == "y" or milk_list[final] == "Y":
			print(f"They might be right. You knew there where metal in the milk. YOU JUST GOT SUED!")
			exit(0)
		else:
			print(f"YOU WIN! Since {things_for_milk[final]}: {milk_list[final]} indicates there is no metal in it, it's under the law requements.")
elif final == 3:
		print(f"They think it's the {things_for_milk[final]} is too long")
		if milk_list[final] > 24:
			print(f"They might be right. The {things_for_milk[final]}: {milk_list[final]} is longer then 24 hours. YOU JUST GOT SUED!")
			exit(0)
		else:
			print(f"YOU WIN! Since {things_for_milk[final]}: {milk_list[final]} is less then 24 hours, it's under the law requements.")

print("Your answers:")
for i in range(0, 3):
	print(things_for_milk[i], ";", milk_list[i])
