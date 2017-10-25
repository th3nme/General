from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Display the filename of the source and destination file.
print "Copying from %s to %s" % (from_file, to_file)

# We could do these on one line, how?
in_file = open(from_file)
indata = in_file.read()

# Open a new empty file and write the source file to it.
out_file = open(to_file, 'w')
out_file.write(indata)

# close the files.
out_file.close()
in_file.close()
