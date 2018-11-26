from sys import argv

script, input_file = argv

# Function to print the entire file passed in the argument using .read()
def print_all(f):
    print(f.read())

# Function to rewind the file passed in the argument back to the beginning
def rewind(f):
    f.seek(0)

# Function to print the line number as well as the contents of that line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file specified with ARGV and assign it to the current_file variable
current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Not let's rewind back to the start like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
