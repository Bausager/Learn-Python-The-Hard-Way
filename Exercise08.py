formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a peom",
	"Or a song about fear"
	))


					# Study Drill

# 1 - 4 Study Drill
format = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(format, format, format, format))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a peom",
	"Or a song about fear"
	))

					# Study Drill from Exercise 07

# 1 - 5 Study Drill

# Defind formatter to be 4 open valriables
formatter = "{} {} {} {}"

# Print and insert 1, ,2 ,3 ,4 into the open valriables.
print(formatter.format(1, 2, 3, 4))
# Print and insert "one", "two", "three", "four" into the open valriables
print(formatter.format("one", "two", "three", "four"))
# Print and inser True, False, False, True (as a string) into the open valriables
print(formatter.format(True, False, False, True))
# Print and insert four open valriables into the open valriables. (Inseption!)
print(formatter.format(formatter, formatter, formatter, formatter))
# Print and insert strings formattet on multiple lines into the open valriables
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a peom",
	"Or a song about fear"
	))
