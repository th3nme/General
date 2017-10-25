from sys import argv

# Gather file name and 3 arguments from command line
script, first, second, third = argv

# Gather fourth variable from raw input prompt
fourth = raw_input("What is the fourth variable?")

# Print the results
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
