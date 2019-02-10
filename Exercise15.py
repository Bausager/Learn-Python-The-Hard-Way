from sys import argv

script, filmename = argv

txt = open(filmename)

print(f"Here's your file {filmename}:")
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())



							# Study Drills
# 1 Study Drill
#
# # Defind how many and what the arguments are when you run the script.
# script, filmename = argv
#
# # Defind txt as the opened file.
# txt = open(filmename)
#
# # Prints a string with the filename in it.
# print(f"Here's your file {filmename}:")
# # Prints the entere open/read file
# print(txt.read())
#
# # Prints a string.
# print("Type the filename again:")
# # Inputs a string, witch is used later. In this case a file name.
# file_again = input('> ')
#
# # Definds and opens the new file witch you have chosen.
# txt_again = open(file_again)
#
# # Prints the entere file, witch you have chosen.
# print(txt_again.read())


# 5 Study Drill
# If you use input, you don't have to hardcode the filename, you just need to run the script

# 7 Study Drill
# script, filmename = argv
#
# txt = open(filmename)
#
# print(f"Here's your file {filmename}:")
# print(txt.read())
#
# txt.close()
#
# print("Type the filename again:")
# file_again = input('> ')
#
# txt_again = open(file_again)
#
# print(txt_again.read())
#
# txt_again.close()
