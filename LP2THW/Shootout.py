import random
from sys import exit
# Ultimate Penalty Shootout
# Author: Nick Ephraims

# Penalty spot, user selects to shoot to the left, middle or right. Goalkeeper choice is random.
# If the shot and goalkeeper choice are the same the shot is saved otherwise it is a goal. 
def penalty_spot():
    print "=" * 80
    print"The opposition have fouled one of your players in the panelty area. The referee awards your team a penalty!"
    print"You have been given the task of converting the penalty. You step up to the penalty spot."
    
    shot_direction = raw_input("Which direction do you shoot. Left, Middle or Right?: ")
    goalkeeper_choice = ['left', 'middle', 'right']
    goalkeeper_decision = random.choice(goalkeeper_choice)

    if shot_direction == goalkeeper_decision:
        miss()
    elif shot_direction in goalkeeper_choice:
        goal()
    else:
        error()

# Shot was successful so it is a goal.
def goal():
    print "=" * 80
    print "IT'S A GOOOOOOOOOOOOOOOOOOAL!!"
    print "You send the keeper in the wrong direction and convert the penalty!!"

    another_attempt = raw_input("Would you like to play again? (Yes / No): ")

    if another_attempt == 'yes':
        penalty_spot()
    else: exit(0)

# Shot was saved so it was a failure.
def miss():
    print "=" * 80
    print "SAAAAAVE!! Oh No!! The keeper correctly guessed where you were shooting the ball and has saved your shot."

    another_attempt = raw_input("Would you like to play again? (Yes / No): ")

    if another_attempt == 'yes':
        penalty_spot()
    else: exit(0)

def error():
    print "That is not a valid shot direction. How about we try that again."
    penalty_spot()

penalty_spot()