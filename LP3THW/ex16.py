from sys import argv

script, filename = argv

print(f"You're about to initialise the file named: {filename}.")
print("If you aren't sure you want to do this now press CTRL-C.")
print("If you would like to proceed press ENTER (or RETURN).")

input("?")

print("Opening and initializing the file now...")
file = open(filename, 'w')

print("Truncating the file... gone")
file.truncate()

print("Please enter 3 lines of text to be written to the file.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
new_lines = f"{line1}\n{line2}\n{line3}\n"

print("Writing the lines you entered into the file...")
file.write(new_lines)

print("OK all done, closing the file now.")
file.close()
