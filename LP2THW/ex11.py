# Ask for age, height and weight input
print "How old are you?",
age = raw_input()
print "How tall are you? (cm's)",
height = raw_input()
print "How much do you weigh? (kg's)",
weight = raw_input()

# Print the input back to the user
print "So, you're %r years old, %r tall and %r heavy." % (
    age, height, weight)
