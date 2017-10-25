# define cheese and crackers function with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# provide the function with static values
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# provide the function with variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# provide the function with the result of some math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# provide the function with both math and variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# ask user how much cheese and crackers they have
cheese = int(raw_input("How many cheeses do you have?"))
crackers = int(raw_input("How many boxes of crackers do you have?"))
cheese_and_crackers(cheese, crackers)
