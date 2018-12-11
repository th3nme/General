total = int(input("How high would you like the count to go?: "))
increment = int(input("What would you like the increment to be?: "))

def create_list(max, increment):
    i = 0
    numbers = []

    for i in range(0, max, increment):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

numbers = create_list((total + increment), increment)

print("The numbers: ")
for num in numbers:
    print(num)
