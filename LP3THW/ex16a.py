from sys import argv

script, filename = argv
txt = open(filename)

print(f"Here's the contents of your file called '{filename}':")
print(txt.read())

print("Now type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(f"Here's the contents of your file called '{file_again}':")
print(txt_again.read())

txt.close()
txt_again.close()
