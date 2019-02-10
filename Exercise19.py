# Definding the funtion with two variables
def cheese_and_crackers(Cheese_count, boxes_of_crackers):
	# prints a string with a variable
	print(f'You have {Cheese_count} cheeses!')
	# prints a string with a variable
	print(f'You have {boxes_of_crackers} boxes_of_crackers!')
	# prints a string
	print("Man that's enough for a party!")
	# prints a string with a new line.
	print("Get a blanket. \n")


# prints a string
print("We can just give the funtion numbers directly:")
# uses the funtion with two numbers
cheese_and_crackers(20, 30)

# prints a string
print("OR, we can use variable from out script:")
# definds a variable
amount_of_cheese = 10
# definds a variable
amount_of_crackers = 50

# calls the funtion with two defind variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# prints a sring
print("We can even do math inside too:")
# calls the funtion with an equation with defind variables
cheese_and_crackers(10 + 20, 5 + 6)

# prints a string
print("And we can combine the two, variables and math:")
# calls the funtion with an equation with defind variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
