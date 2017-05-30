#we are setting a vaulue for the variables with words and numbers.
cars = 100 
space_in_a_car = 4.0
drivers = 30
passangers = 90
#we are setting a values for variables with words
cars_not_driven = cars - drivers
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passangers / cars_driven

#the math equation taking place, with the console reading the strings as words and the variables as numbers
print "there are", cars, "cars availale"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driven, "empty cars today."
print "we can trnasport", carpool_capacity, "people today."
print "we have", passangers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."

#What i believe the error is saying is that 'car_pool_capacity' is not a defined variable
#so it was not able to do the equation. on line 8 where the error presents the math equation was
#written in a wrong way.
# Traceback (most recent call last):
# 	file "ex4.py", line 8, in <module>
#		average_passengers_per_car = car_pool_capacity / passenger
#	NameError: name 'car_pool_capacity' is not defined