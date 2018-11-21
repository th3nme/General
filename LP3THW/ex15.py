from sys import argv

# Gather the filename you want to open from the command line
script, filename = argv

# Open the file specified when running the script and assign it to the txt variable
txt = open(filename)

# Print the contents of the file that was loaded into the txt variable
print(f"Here's the contents of your file called '{filename}':")
print(txt.read())

# Ask the user to enter the filename again so we can get it from user import isntead of argv
print("Now type the filename again:")
file_again = input("> ")

# Open the file specified when running the script and assign it to the txt_again variable
txt_again = open(file_again)

# Print the contents of the file that was loaded into the txt_again variable
print(f"Here's the contents of your file called '{file_again}':")
print(txt_again.read())

# Now that we have finished printing the files we are going to close them
txt.close()
txt_again.close()
