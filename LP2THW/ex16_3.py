from sys import argv

# Use filename and one command line argument to use with argv
script, filename = argv

# Inform the user that they are abot to delete the file specified in the
# argument and whether to proceed or abort
print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)."
print "If you do what to do that, hit ENTER."

# Wait for user to confirm or exit
raw_input("?")

# Open the file names in command argument
print "Opening the file..."
target = open(filename, 'w')

# Truncates the file if it already exists.
# The most commonly-used values of mode are
# 'r' for reading,
# 'w' for writing (truncating the file if it already exists), and
# 'a' for appending
print "Truncating the file. Goodbye!"
target.truncate()

# Ask the user to input 3 lines of text
print "Now I'm going to ask you for 3 lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Write the 3 inputted lines to a file on seperate lines.
print "I'm going to write this to the file."
target.write("%s \n%s \n%s" % (line1,line2,line3))

# Close the file
print "And finally, we close it."
target.close()
