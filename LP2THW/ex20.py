from sys import argv

script, input_file = argv

# define print_all function which prints the whole file
def print_all(f):
    print f.read()

# definte the rewind function which does back to the start of the file
def rewind(f):
    f.seek(0)

# definte print_a_line function which prints a specific line
def print_a_line(line_count, f):
    print line_count, f.readline()

# assigns the file from command line argument to current_file variable
current_file = open(input_file)

# prints the entire file
print "First, let's print the whole file:\n"
print_all(current_file)

# go back to the start of the file
print "Now, let's rewind, kind of like a tape."
rewind(current_file)

# print each line in the file using a function and adding 1 to the current line
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
