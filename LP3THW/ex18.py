# This function takes arguments like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"Arg1: {arg1}, Arg2: {arg2}")

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"Arg1: {arg1}, Arg2: {arg2}")

# This function takes only one argument
def print_one(arg1):
    print(f"Arg1: {arg1}")

# This one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Nick", "Ephraims")
print_two_again("Nick", "Ephraims")
print_one("First!")
print_none()
