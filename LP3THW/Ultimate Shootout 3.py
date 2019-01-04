import random
from sys import exit
# Ultimate Penalty Shootout 3
# Author: Nick Ephraims

# We have a penalty spot kick. The player selects from 3 options and the goalkeeper selects randomly.
# If there is a match the shot is saved otherwise a goal is scored

# Function for penalty shot randomizer / score keeper game engine
# function for player spot kick
# second function for player goal keeper AI shot randomizer
# seperate functions for goal scored, goal missed, goal saved, goal conceded. 
# invalid response slipped voer and booted ball into the stands
# if x shots remaining and score difference is + or - certain amount then exit

print("=" * 80)
print("You are playing in the Football World Cup Final! Extra time is over but the scores are still tied.")
print("That means the match will be decided in a penalty shootout! Both teams line up along the half way line.")
print("The referee blows his whistle, its a PENALTY! The crowd roars continuously.")
print("The atmosphere is reaching fever pitch! The crowd is going ballistic. It all comes down to this")
print("=" * 80)

def shootout_engine():
    print("=" * 80)
    # Number of shots taken by each team
    player_shots = 0
    computer_shots = 0
    # Number of goals scored by each team
    player_score = 0
    computer_score = 0

    while player_shots + computer_shots <= 9 
        if player_shots == computer_shots
            penalty_shoot()
        else:
            penalty_defend()
    
    while player_shots + computer_shots >= 10 
        if player_score != computer_score and player_shots == computer_shots


def penalty_defend():
    print("=" * 80)

def penalty_shoot():
    print("=" * 80)

def goal_scored_():
    print("=" * 80)

def goal_saved():
    print("=" * 80)

def error():
    print("=" * 80)

shootout_engine()
