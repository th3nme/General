# Set static values
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# Calculate the numbers of cars not being driven
cars_not_driven = cars - drivers

# Calculate the number of cars driven which is equal to the number of drivers
cars_driven = drivers

# Calculate the carpool capacity by multiplying the space in each car by the
# total numbers of cars being driven
carpool_capacity = cars_driven * space_in_a_car

# Calculate the average passengers per car by dividing the total passengers
# by the number of cars being driven
average_passengers_per_car = passengers / cars_driven

# Print results
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to transport today."
print "We need to put about", average_passengers_per_car, "in each car."
