from sys import exit

def gold_room():
    print("This rom is full of gold. How much do you take?")

def bear_room():
    print("There is a bear in here")

def cthulhu_room():
    print("There you see the great evil Cthulhu.")

def dead(why):
    print(why, "Oh dear...!")
    exit(0)

def start():
    print("You are in a dark room.")

start()
