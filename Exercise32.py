the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pinnies", 2, "dimes", 3, "quaters"]

# This first kind of for-loop goes through a list
for number in the_count:
	print(f"This is count {number}.")

# Same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}.")

# Also we can go through mixed lists too.
# Notive we have to use {} since we don't know what's in it.
for i in change:
	print(f"I got {i}.")

# We can also biuld lists, fist start with an empty one.
elements = []

for i in range(0, 6):
	print(f"Adding {i} to the list.")
	# Append is a function that lists understand.
	elements.append(i)

# Now we can print them out too
for i in elements:
	print(f"Elements was: {i}")


# The answer is no.
list = range(0, 10)

print(list)
