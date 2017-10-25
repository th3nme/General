from sys import argv

# Call the script name and the filename from command line argument
script, filename = argv

# Open the text file from command line argument
txt = open(filename)

# Print the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# Ask the user to input the filename to read
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file that the user specifies
txt_again = open(file_again)

# Print the file contents
print txt_again.read()

# Close the files we opened
txt.close()
txt_again.close()
