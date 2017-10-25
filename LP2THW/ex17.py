from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Display the filename of the source and destination file
print "Copying from %s to %s" % (from_file, to_file)

# We could do these on one line, how?
in_file = open(from_file)
indata = in_file.read()

# Print the size of the file in bytes
print "The input file is %d bytes long" % len(indata)

# Checks to see if the destination file already exists and returns true or false
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN (Enter) to continue, CRTL-C to abort."
raw_input()

# Open a new empty file and write the source file to it.
out_file = open(to_file, 'w')
out_file.write(indata)

# Display completion message and close both open files
print "Alright, all done."
out_file.close()
in_file.close()
