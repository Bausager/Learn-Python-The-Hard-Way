# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass


# Dog has-a __init__ that takes self and name parameters.
class Dog (Animal):

	def __init__(self, name):
		# Dog has-a name
		self.name = name


# Cat has-a __init__ that takes self and name parameters.
class Cat(Animal):

	def __init__(self, name):
		# Cat has-a name
		self.name = name


#
class Person(object):

	def __init__(self, name):
		# Person has-a name
		self.name = name

		# Person has-a pet of some kind
		self.pet = None


#
class Employee(Person):

	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary


class Fish:

	def __init__(self, fish, eaten=None):
		self.fish = fish
		if eaten is None:
			self.eaten = []
		else:
			self.eaten = eaten


	def add_eaten(self, eat):
		new = eat.split(', ')
		for i in range(len(new)):
			if new[i] not in self.eaten:
				self.eaten.append(new[i])


	def remove_eaten(self, eat):
		new = eat.split(', ')
		for i in range(len(new)):
			if new[i] in self.eaten:
				self.eaten.remove(new[i])


class Salmon(Fish):
	pass


class Halibut(Fish):
	pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# Marry has-a Cat named Satan
mary.pet = satan

# frank is an Employee with a 120000 salary
frank = Employee("Frank", 120000)

# Frank has a pet, rover, who's a dog
frank.pet = rover

# flipper is-a Fish.
flipper = Fish("Red thingy", ["grass", "flowers"])

print(flipper.fish)
print(flipper.eaten)
flipper.add_eaten("new thing, four more")
print(flipper.eaten)
flipper.remove_eaten("grass, flowers")
print(flipper.eaten)

# croise is-a Salmon()
crouse = Salmon("new")

# harry is-a Hailbut
harry = Halibut("What")


print()
