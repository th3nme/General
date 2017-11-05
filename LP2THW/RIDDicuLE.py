# RIDDicuLE
# Author: Nick Ephraims

from sys import exit
from random import randint

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
        raw_input("> ")
        return 'first_floor'

class FirstFloor(Level):
    
    def enter(self):
        print "=" * 60

class SecondFloor(Level):
    
    def enter(self):
        pass

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
    }
    
    def __init__(self, start_level):
        self.start_level = start_level

    def next_level(self, level_name):
        val = Map.levels.get(level_name)
        return val

    def opening_level(self):
        return self.next_level(self.start_level)

def random_riddle():
    
    riddles = {

    }


a_map = Map('basement')
a_game = Engine(a_map)
a_game.play()