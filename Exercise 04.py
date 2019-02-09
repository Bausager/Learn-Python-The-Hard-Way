cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / drivers


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")



										# Study Drill

							# (1) Study Drill, it's wothout a number.
# If you havn't defind what carpool_capacity is, with a =, you can't use it in a calculation. It's like x + 2 and you/python expects a number output

							# 1 and 2 Study Drill
# It takes it as a int insted of a float. Witch means it can't caltulate it with decimals

							# 3 Study Drill
# The number of cars available
cars = 100
# the space inside of the cars
space_in_a_car = 4.0
# Drivers available
drivers = 30
# Total number of passengers
passengers = 90
# The number of cars not driven
cars_not_driven = cars - drivers
# The number of cars driven
cars_driven = drivers
# The total inside capacity in the driven cars
carpool_capacity = cars_driven * space_in_a_car
# The average number of people/passengers per car
average_passengers_per_car = passengers / drivers
