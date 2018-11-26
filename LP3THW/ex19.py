# Create the function to print how much cheese and crackers we have based on the arguments provided
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} pieces of cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a picnic!\n")

# Give specific numbers as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Give variables as arguments
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Perform mathematics before giving the results as an argument
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Use variables with math first and then provide the results as arguments
print("And we can combine the variables and math together:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
