"""RIDDicuLE The Game"""
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
    if chances_remaining == 0:
        deaths = [
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
        print deaths[randint(0, len(deaths)-1)]
        exit()

class Level(object):
    """Parent class of game levels (not used yet)"""
    def enter(self):
        """Nothing"""
        print "This class is not yet configured."
        exit(1)

class Engine(object):
    """Engine controls which class is the current level and runs it accordingly"""
    def __init__(self, level_map):
        self.level_map = level_map

    def play(self):
        """Runs the current level"""
        current_level = self.level_map.opening_level()
        last_level = self.level_map.next_level('rooftop')

        while current_level != last_level:
            next_level_name = current_level.enter()
            current_level = self.level_map.next_level(next_level_name)
        # Be sure to print out the last level
        current_level.enter()

class Basement(Level):
    """First level"""
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
        print "see if there is another way out."
        print "=" * 60
        raw_input("'Enter'> ")
        return 'first_floor'

class FirstFloor(Level):
    """Undead zombie level"""
    def enter(self):
        print "=" * 60
        print "You enter the room and notice the doors leading outside are chained shut."
        print "You hear a scraping noise and turn around. A horrible zombie like creature"
        print "hobbles towards you. Its skin is grey and rotting showing bone and flesh"
        print "in some places. Its pupil-less eyes glow with a dim white luminescence."
        print "In a raspy voice the undead creature tells you that you will be allowed to"
        print "pass if you correctly answer a riddle in 3 attempts. If you fail it will"
        print "bite you spreading the disease and you too will become an undead zombie."
        print "=" * 60
        raw_input("'Enter'> ")
        random_riddle()
        print "The undead zombie steps aside and you take the stairs up to the next floor."
        return 'second_floor'

class SecondFloor(Level):
    """Giant snake level"""
    def enter(self):
        print "Second floor"
        random_riddle()
        return 'third_floor'

class ThirdFloor(Level):
    """Medusa level"""
    def enter(self):
        print "Third floor"
        random_riddle()
        return 'fourth_floor'

class FourthFloor(Level):
    """Minotaur level"""
    def enter(self):
        print "Fourth floor"
        random_riddle()
        return 'fifth_floor'

class FifthFloor(Level):
    """Giant spider level"""
    def enter(self):
        print "Fitfh floor"
        random_riddle()
        return 'sixth_floor'

class SixthFloor(Level):
    """Demon level"""
    def enter(self):
        print "Sixth floor"
        random_riddle()
        return 'seventh_floor'

class SeventhFloor(Level):
    """Dracula level"""
    def enter(self):
        print "Seventh floor"
        random_riddle()
        return 'eighth_floor'

class EighthFloor(Level):
    """Giant Squid level"""
    def enter(self):
        print "Eighth floor"
        random_riddle()
        return 'ninth_floor'

class NinthFloor(Level):
    """T-Rex level"""
    def enter(self):
        print "Ninth floor"
        random_riddle()
        return 'tenth_floor'

class TenthFloor(Level):
    """Godzilla level"""
    def enter(self):
        print "Tenth floor"
        random_riddle()
        return 'rooftop'

class Rooftop(Level):
    """Escape Helicopter level"""
    def enter(self):
        print "You win"
        exit(0)

class Map(object):
    """Level map"""
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