from sys import argv

script, filmename = argv

txt = open(filmename)

print(f"Here's your file {filmename}:")
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
