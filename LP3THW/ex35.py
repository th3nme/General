from sys import exit

def gold_room():
    print("This rom is full of gold. How much do you take?")

    choice = int(input("> "))
    
    if choice < 50:
        print("You're level of greed is acceptible. You may keep the gold!")
        exit(0)
    else:
        dead("That's too much you greedy bastard!")


def bear_room():
    print("There is a big angry bear in here blocking the door!")
    print("The bear has a large jar of honey infront of it.")
    print("How are you going to get past the bear without dying?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear howls with rage and swipes you arrcoss the face severing your arteries!")
        elif choice == "taunt bear" and not bear_moved:
            print("You taunt the bear. It get's up on its feet slowly alowing access to the door")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets angry and claws your leg's off!")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("Input not valid, try again.")


def cthulhu_room():
    print("There you see the great evil Cthulhu.")
    print("He, It, whatever it is stares at you as you start to go insane.")
    print("Do you flee or eat your own head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Mmmm, tasty!")
    else: cthulhu_room()


def dead(why):
    print(why, "Oh dear...!")
    exit(0)


def start():
    print("You wake up in a dark room.")
    print("There are 2 doors. One to the left and one to the right.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around in the dark until you starve to death.")


start()
