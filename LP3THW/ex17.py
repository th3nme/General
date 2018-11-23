from sys import argv
from os.path import exists

script, source_file, destination_file = argv

print(f"Copying data from {source_file} to {destination_file}")

# We could do these 2 steps on one line, how?
input_file = open(source_file)
input_data = input_file.read()
#input_data = input_file.read(open(source_file))

print(f"The source file is {len(input_data)} bytes long")

print(f"Does the output file exist? {exists(destination_file)}")
print("If yes press ENTER to proceed else press CRTL-C to Abort.")
input()

output_file = open(destination_file, 'w')
output_file.write(input_data)

print(f"Data has been copied from {source_file} to {destination_file}!")

output_file.close()
input_file.close()

#open(output_file, 'w').write(open(source_file).read())
