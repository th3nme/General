# RIDDicuLE
# Author: Nick Ephraims

from sys import exit
from random import randint
import random

def random_riddle():
    """Generate 3 random riddles from a dict for player to solve"""
    riddles = {
        "Poor people have it, Rich People need it. If you eat it you die.":
            "nothing",
        "Mary's father has 5 daughters. Nana, Nene, Nini, Nono and ____. "
        "What is the fifth daughters name?":
            "mary",
        "How can a pants pocket be empty and still have something in it?":
            "hole",
        "What word becomes shorter when you add two letters to it?":
            "short",
        "If I have it, I haven't shared it. If I share it, I don't have it anymore.":
            "secret",
        "What has hands but can't clap?":
            "clock",
        "What can you catch but not throw?":
            "cold",
        "What is so delicate that just saying its name will break it?":
            "silence",
        "What starts with 't', is filled with 't' and ends with 't'?":
            "teapot",
        "How many months have 28 days?":
            "twelve",
        "I am buried alive and dug up when dead.":
            "tree",
        "Sometimes I walk in front some I walk behind. Is is only in the dark that "
        "I ever leave you":
            "shadow",
        "I weigh almost nothing but cannot be heald for long.":
            "breath",
        "I can be seen in water but I never ge wet.":
            "reflection",
        "The more you take, the more you leave behind":
            "footsteps",
        "What has many keys but can't open any doors?":
            "piano",
        "Tall I am young, short I am old. While alive I glow, wind is my foe.":
            "candle",
        "You answer me but I ask no questions.":
            "phone",
        "What can travel around the world but never leave the corner?":
            "stamp",
        "What occurs once every minute, twice every moment but never in a thousand years?":
            "m",
        "The more it dries, the wetter it gets.":
            "towel",
        "What is always coming but never arrives?":
            "tomorrow",
        "When spelt forwards I am heavy. When spelt backward I am not":
            "ton",
        "What belongs to you but is more commonly used by others":
            "name",
        "It can run but can't walk and has a mouth but can't talk. "
        "It has a head but can't think and a bed but can't sleep":
            "river",
        "Until I am measured, I am not known, yet how you miss me when I have flown.":
            "time",
        "It cannot be seen, cannot be felt. Cannot be heard, cannot be smelt."
        "It lies behind stars, under hills and empty holes it fills.":
            "darkness",
        "A box without hinges, key or lid. Yet golden treasure inside is hid.":
            "egg",
        "Feed me and I live, give me a drink and I die.":
            "fire",
        "Which word is always spelt incorrectly?":
            "incorrectly",
    }
    
    # Give the player 3 chances to give a correct answer
    chances_remaining = 3
    correct_answer_given = False

    # Ask random riddle until correct answer or 3 incorrect answers are given 
    while chances_remaining > 0 and correct_answer_given == False:
        # Get a random riddle and answer from riddles{}
        question = random.choice(list(riddles.keys()))
        correct_answer = riddles.get(question)
        print "=" * 60
        # Display the riddle and prompt player for the answer
        print "[Riddle]: %s" % question
        answer = raw_input("[Answer]: ")
        # If answer is not correct then ask a new riddle and subtract 1 from chances_remaining
        if answer.lower() != correct_answer.lower():
            chances_remaining -= 1
            print "The creature deems that your answer is either incorrect or too long"
            print "You now have %s chance(s) left" % chances_remaining
        else:
            # If answer is correct mark correct answer given as True
            correct_answer_given = True
            print "The creature accepts your answer as correct."
            print "You are allowed to live a little bit longer."
    # If you player runs out of chances they die or if not they win and move to the next level
    if chances_remaining == 0:
        return 'death'
    else:
        pass

class Level(object):
    
    def enter(self):
        print "This class is not yet configured."
        exit(1)

class Engine(object):
    
    def __init__(self, level_map):
        self.level_map = level_map

    def play(self):
        current_level = self.level_map.opening_level()
        last_level = self.level_map.next_level('rooftop')

        while current_level != last_level:
            next_level_name = current_level.enter()
            current_level = self.level_map.next_level(next_level_name)
        
        # Be sure to print out the last level
        current_level.enter()

class Death(Level):
    
    quips = [
        "The creature deems your answers to be insufficient and decides to" 
        "rip your head clean off. Oh No! It appears that you are dead.",
        "The creature ponders our response briefly but ultimately decides"
        "that it doesn't like your answers and fly kicks you right in the face."
        "Your head is parted from your shoulders killing you instantly",
        "The creature licks its lips and after a brief moment decides that your"
        "answers are wrong and races towards you and a frightening pace. It tears"
        "your body limb from limb before chewing your flesh leaving nothing"
        "but clean bones behind. Guess that means youe dead!"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Basement(Level):
    
    def enter(self):
        print "=" * 60
        print "You wake up in a basement, head throbbing and unable to remember"
        print "how you got here. Random body parts belonging to at least a dozen"
        print "people litter the floor. You take a closer look at some of the"
        print "body parts and notice what seems to be a variety of teeth and"
        print "claw marks. You hear a groaning noise and realise you're not alone."
        print "You find a person that appears to be severly injured and near death."
        print "As you approach they start rambling about riddles, short answers and"
        print "three chances... perhaps this will make sense later. You notice that"
        print "the only way out is a staircase heading upstairs so you decide to"
        print "see if there is a way out upstairs."
        print "=" * 60
        raw_input("'Enter'> ")
        return 'first_floor'

class FirstFloor(Level):
    """Undead zombie level"""
    def enter(self):
        print "=" * 60
        random_riddle()
        return 'second_floor'

class SecondFloor(Level):
    
    def enter(self):
        print "second floor"

class ThirdFloor(Level):
    
    def enter(self):
        pass

class FourthFloor(Level):
    
    def enter(self):
        pass

class FifthFloor(Level):
    
    def enter(self):
        pass

class SixthFloor(Level):
    
    def enter(self):
        pass

class SeventhFloor(Level):
    
    def enter(self):
        pass

class EighthFloor(Level):
    
    def enter(self):
        pass

class NinthFloor(Level):
    
    def enter(self):
        pass

class TenthFloor(Level):
    
    def enter(self):
        pass

class Rooftop(Level):
    
    def enter(self):
        pass

class Map(object):
    
    levels = {
        'basement': Basement(),
        'first_floor': FirstFloor(),
        'second_floor': SecondFloor(),
        'third_floor': ThirdFloor(),
        'fourth_floor': FourthFloor(),
        'fifth_floor': FifthFloor(),
        'sixth_floor': SixthFloor(),
        'seventh_floor': SeventhFloor(),
        'eighth_floor': EighthFloor(),
        'ninth_floor': NinthFloor(),
        'tenth_floor': TenthFloor(),
        'rooftop': Rooftop(),
        'death': Death(),
    }
    
    def __init__(self, start_level):
        self.start_level = start_level

    def next_level(self, level_name):
        val = Map.levels.get(level_name)
        return val

    def opening_level(self):
        return self.next_level(self.start_level)

a_map = Map('basement')
a_game = Engine(a_map)
a_game.play()