my_name = 'Nick Ephraims'
my_age = 28
my_height = 192
my_weight = 95
my_weight_pounds = round(my_weight * 2.2)
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} centimeters tall.")
print(f"He weighs {my_weight} kilograms or {my_weight_pounds} pounds.")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = my_age + my_height + my_weight
print(f"If I add his age: {my_age}, height: {my_height} and weight: {my_weight} I get a total of: {total}")
