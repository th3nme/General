name = 'Nick Ephraims'
age = 28
height = 192
weight = 95
weight_pounds = round(weight * 2.2)
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He weighs {weight} kilograms or {weight_pounds} pounds.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add his age: {age}, height: {height} and weight: {weight} I get a total of: {total}")
