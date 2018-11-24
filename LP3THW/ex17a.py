from sys import argv

script, source_file, destination_file = argv

open(destination_file, 'w').write(open(source_file).read())
