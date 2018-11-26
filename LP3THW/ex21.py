def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} x {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(20, 8)
height = subtract(200, 8)
weight = multiply(16, 6)
iq = divide(800, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here's the puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

print("what = add(age, subtract(height, multiply(weight, divide(iq, 2))))")
print("what = add(age, subtract(height, multiply(weight, divide(400, 2))))")
print("what = add(age, subtract(height, multiply(96, 200)))")
print("what = add(age, subtract(192, 19200))")
print("what = add(28, -19008)")
print("what = -18980")
