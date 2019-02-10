from sys import argv

# script, filename = argv
#
# print(f"We're going to erase {filename}.")
# print("If you don't want that, hit CTRL-C (^C).")
# print("If you do want that, hit RETURN.")
#
# input("?")
#
# print("Opening the file...")
# target = open(filename, 'w')
#
# print("Truncating the file. Goodbye!")
# target.truncate()
#
# print("Now I'm going to ask you for three lines.")
#
# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")
#
# print("I'm going to write these to the file.")
#
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')
#
# print("And finally, we close it.")
# target.close()


			# Study Drills
# 1 Study Drill

filename = input("What is the filename? \n > ")
target = open(filename, 'r')

print(f"The data in {filename}:\n")
print(target.read(), "\n")

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")


print("Truncating the file. Goodbye!")
target = open(filename, 'w')  # the 'w' delets the data

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}")

target = open(filename, 'r')

print("New file:\n")
print(target.read(), "\n")

print("And finally, we close it.")
target.close()
