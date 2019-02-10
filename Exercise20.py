# imports the argv module
from sys import argv

# define argv
script, input_file = argv


# definds a funtion
def print_all(f):
	# reads the hole file
	print(f.read())


# definds a funtion
def rewind(f):
	# Makes it read from the start again
	f.seek(0)


# definds a funtion
def print_a_line(line_count, f):
	# prints witch line it is, and since it hasn't reset, it will print line after line
	print(line_count, f.readline(), end='')
	# adds one to the line_count
	line_count += 1


# opens the file to current_file
current_file = open(input_file)

# prints a string
print("First let's print the whole file:\n")

# prints the whole file
print_all(current_file)

# prints a string
print("Now let's rewind, kind of like a tape.")

# resets it to read from the start
rewind(current_file)

# prints a string
print("Let's print three line:")

# definds current_line as 1
current_line = 1
# prints from the funtion, the line count and the first line from the file
print_a_line(current_line, current_file)

# prints from the funtion, the line count and the second line from the file
print_a_line(current_line, current_file)

# prints from the funtion, the line count and the third line from the file
print_a_line(current_line, current_file)
