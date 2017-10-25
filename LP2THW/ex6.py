# Define x
x = "There are %d types of people." % 10

# Define binary
binary = "binary"

# Define do_not
do_not = "don't"

# Define y
y = "Those who know %s and those who %s." % (binary, do_not)

# Print x and y
print x
print y

# Print x and y again with extra text
print "I said: %r." % x
print "I also said: '%s'." % y

# Define hilarious as False
hilarious =True

# Define joke evaluation
joke_evaluation = "Isn't that joke so funny? %r"

# Print joke evaluation + hilarious
print joke_evaluation % hilarious

# Define w and e
w = "This is the left side of..."
e = " a string with a right side."

# Print w and e
print w + e
