# Define the formatter variable with 4 x formats
formatter = "{} {} {} {}"

# Call the formatter variable and pass it 4 x arguments and then print out the result
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Everything about you is how I want to be",
    "\nYour freedom comes naturally",
    "\nEverything about you resonates happiness",
    "\nNow I won't settle for less"
))
