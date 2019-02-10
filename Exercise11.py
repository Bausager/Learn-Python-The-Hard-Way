print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


					# Study Drill
print("What's your height?", end=' ')
height = int(input())
print("How heigh do you want to be?", end=' ')
wish = int(input())

if height > wish:
	print("You need to have", height - wish, "cut off!")
elif wish > height:
	print("You're missing", wish - height, "grow up!")
else:
	print("Nothing more to say")
