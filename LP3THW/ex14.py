from sys import argv

script, user_name, age = argv
answer = 'Answer: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(answer)

print(f"Where do you live {user_name}?")
lives = input(answer)

print("What kind of computer do you have?")
computer = input(answer)

print(f"""
Alrighty, so you said {likes} about liking me.
Your {age} and live in {lives}. That's a pretty cool place!
You also have a {computer} computer. That's awesome!
""")
