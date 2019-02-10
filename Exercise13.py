from sys import argv
# read the WYSS section how to run this
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variavle is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# $ python3.6 Exercise13.py first 2nd 3rd

# 2 - 4 Study Drill
script, x1, x2, x3 = argv

print("What's your age?:", x1)
print("What's your height?:", x2)
print("Are you fit?:", x3)
random_variable = int(input("Give a a random number: "))

print("Magic number!: ", random_variable * int(x1))

# $ python3.6 Exercise13.py 23 169 yes
