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
        currnet_level = self.level_map.opening_level()
        last_level = self.level_map.next_level('rooftop')

        while current_level != last_level:
            next_level_name = current_level.enter()
            current_level = self.level_map.next_level(next_level_name)
        
        # Be sure to print out the last level
        current_level.enter()

class Basement(Level):
    
    def enter(self):
        print "You wake up in a basement, head throbbing and unable to remember how you got here."
        print "Random body parts belonging to at least a dozen people litter the floor."

class FirstFloor(Level):
    
    def enter(self):
        pass

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
        pass

    def opening_level(self):
        pass

def random_riddle():
    
    riddles = {

    }


a_map = Map('basement')
a_game = Engine(a_map)
a_game.play()