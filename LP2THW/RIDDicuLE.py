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
        "I weigh almost nothing but cannot be held for long.":
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
        print "=" * 80
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
            "The creature deems your answers to be insufficient and decides to\n"
            "rip your head clean off. Oh No! It appears that you are dead.",
            "The creature ponders our response briefly but ultimately decides\n"
            "that it doesn't like your answers and fly kicks you right in the face.\n"
            "Your head is parted from your shoulders killing you instantly",
            "The creature licks its lips and after a brief moment decides that your\n"
            "answers are wrong and races towards you and a frightening pace. It tears\n"
            "your body limb from limb before chewing your flesh leaving nothing\n"
            "but clean bones behind. Guess that means youe dead!"
        ]
        print "=" * 80
        print deaths[randint(0, len(deaths)-1)]
        print "GAME OVER!"
        print "=" * 80
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
        print "=" * 80
        print "You wake up in a basement, head throbbing and unable to remember"
        print "how you got here. Random body parts belonging to at least a dozen"
        print "people litter the floor. You take a closer look at some of the"
        print "body parts and notice what seems to be a variety of teeth and"
        print "claw marks. You hear a groaning noise and realise you're not alone."
        print "You find a person that appears to be severly injured and near death."
        print "As you approach they start rambling about riddles, short answers and"
        print "three chances... perhaps this will make sense later. You notice that"
        print "the only way out is a staircase heading upstairs so you decide to"
        print "see if there is another way out..."
        print "=" * 80
        raw_input("'Enter'> ")
        return 'first_floor'

class FirstFloor(Level):
    """Undead zombie level"""
    def enter(self):
        print "=" * 80
        print "You enter the room and notice the doors leading outside are chained shut."
        print "You hear a scraping noise and turn around. A horrible zombie like creature"
        print "hobbles towards you. Its skin is grey and rotting showing bone and flesh"
        print "in some places. Its pupil-less eyes glow with a dim white luminescence."
        print "In a raspy voice the undead creature tells you that you will be allowed to"
        print "pass if you correctly answer a riddle in 3 attempts. If you fail it will"
        print "bite you spreading the disease and you too will become an undead zombie..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The undead zombie steps aside and you take the stairs up to the next floor."
        raw_input("'Enter'> ")
        return 'second_floor'

class SecondFloor(Level):
    """Giant snake level"""
    def enter(self):
        print "=" * 80
        print "You reach the top of the stairs and almost trip over a strange carpet roll."
        print "After you regain your footing you realise it is infact a discarded Basilisk skin."
        print "Judging by the size of the discarded skin you estimate the creature at over 20"
        print "metres long. To back up this fact you hear a feint hissing sound getting nearer."
        print "As you round a corner you quickly shut your eyes when you remember that looking"
        print "a Basilisk directly in the eye causes instant death. The Basilisk wraps around"
        print "you and traps you in place. You try to relax your mind for the next riddle as the"
        print "Basilisk grips you tighter and tighter..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The Basilisk releases its grip, allowing you to go up to the next floor."
        raw_input("'Enter'> ")
        return 'third_floor'

class ThirdFloor(Level):
    """Dragon level"""
    def enter(self):
        print "=" * 80
        print "You exit the stairwell and immediately start sweating due to the intense heat"
        print "permeating the room. You notice various scorth marks on the floor when out of"
        print "nowhere a large scaly tail smacks into you pinning you up against a wall."
        print "After being briefly dazed you open your eyes to see the huge gaping maw of"
        print "of a massive dragon filling your field of view. The dragon unleashes a loud"
        print "deafening roar right in your face. You feel the intense heat generated by the"
        print "dragon and realise you will be burnt to a crisp in seconds unless you can give"
        print "the creature a satisfactory answer..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The dragon roars again in anger but releases you and allows you to move on."
        raw_input("'Enter'> ")
        return 'fourth_floor'

class FourthFloor(Level):
    """Minotaur level"""
    def enter(self):
        print "=" * 80
        print "You enter the next room cautiously scanning for threats. You hear a noise behind"
        print "you and turn to see a horrible beast, half man half bull charging towards you"
        print "weilding a massive axe. The Minotaur stops right infront of you and raises the"
        print "axe threateningly. Judging by its well muscled physique and the crazed look in"
        print "its eyes you decide that it would not have much difficulty parting your head from"
        print "your shoulders. The Minotaur backs you into a corner cutting off your escape..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The Minotaur lowers its axe and steps aside. You move onto the next floor."
        raw_input("'Enter'> ")
        return 'fifth_floor'

class FifthFloor(Level):
    """Giant spider level"""
    def enter(self):
        print "=" * 80
        print "You step through the door and get caught up immediately in something sticky."
        print "It appears to be some kind of spiders web covering the floor, walls and ceiling."
        print "Before you can do anything else a pair of long hairs legs grab you around your"
        print "midsection and lift you towards a pair of giant fangs surrounded by lots of"
        print "scary looking eyes! The gigantic spider makes a clicking noise with its fangs"
        print "as if it is about to make a meal out of you..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The giant spider releases its grip and you fall to the floor as it scurries away."
        raw_input("'Enter'> ")
        return 'sixth_floor'

class SixthFloor(Level):
    """Demon level"""
    def enter(self):
        print "=" * 80
        print "You enter the room which strangly, appears to be empty. All of a sudden a portal"
        print "opens up next to you. Through the portal steps a huge Demon. Red leathery skin,"
        print "black wings, long pointy tail and large horns. This is truely a creature of"
        print "nightmares. The Demon summons an enormous blade in each hand, walks over to you"
        print "and rests the blades on either side of your neck. The slightest movement could"
        print "end you..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The Demon removes the blades from your neck and steps back through the portal"
        print "from whence it came, once again leaving you in an empty room. You proceed at once."
        raw_input("'Enter'> ")
        return 'seventh_floor'

class SeventhFloor(Level):
    """Dracula level"""
    def enter(self):
        print "=" * 80
        print "You step through the door into a room filled with an eerie unnatural fog. A large"
        print "black Bat flies at you out of the fog. You raise your hands in defence but realise"
        print "the bat is no longer there but rather the tall imposing figure of a man. He has"
        print "pale white skin, and large kanine teeth protruding over the bottom lip. You realise"
        print "He is a Vampire. Not just any Vampire but Dracula himself! With astonishing speed"
        print "He traps you in an embrace and extends his fangs over your jugular vein. He seems"
        print "thirsty..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The vampire releases you, transforms into a bat and flies away unsatisfied."
        raw_input("'Enter'> ")
        return 'eighth_floor'

class EighthFloor(Level):
    """Giant Squid level"""
    def enter(self):
        print "=" * 80
        print "You enter the room and almost slip over. The entire floor is covered with water."
        print "There is also a foul stench of rotting fish in the air. Before you have time to"
        print "do anything a long tentacle covered in suction cups whips out ans grasps you by"
        print "the leg. Another tentacle grabs you and you are brought within inches of a razor"
        print "sharp beak. The stench here is unbearable. The giant squid looks at you with a"
        print "dead expressionless eye..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The giant squid releases its grip and allows you to continue."
        raw_input("'Enter'> ")
        return 'ninth_floor'

class NinthFloor(Level):
    """Tyrannosaurus Rex level"""
    def enter(self):
        print "=" * 80
        print "You exit the stairs into the room and trip over almost straight away. As you stand"
        print "up you are confronted by a ferocious Tyrannosaurus Rex! It has frightening claws and"
        print "row upon row of razor sharp teeth. The T-Rex approaches you slowly as if savouring"
        print "the moment. It clearly expects that you will be its next meal. With one of its"
        print "powerful legs it pins you to the floor and lets out a loud roar..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "The T-Rex decides to be a vegetarian and lets you pass unharmed."
        raw_input("'Enter'> ")
        return 'tenth_floor'

class TenthFloor(Level):
    """Godzilla level"""
    def enter(self):
        print "=" * 80
        print "You dust yourself off and move to the next floor. You think you must surely be"
        print "getting close to the rooftop where you might be able to escape. As you enter the"
        print "next floor you find several large eggs, almost as tall as you are. Whatever laid"
        print "these eggs must be massive. As if to confirm your suspicion a massive ear splitting"
        print "roar fills the room. You follow the sound and are horrified to see Godzilla"
        print "approaching. It looms tall over you and you feel that if you move it might just be"
        print "the last thing you do..."
        print "=" * 80
        raw_input("'Enter'> ")
        random_riddle()
        print "Godzilla moves aside but you get the feeling this might not be over yet. You head"
        print "upstairs to the rooftop."
        raw_input("'Enter'> ")
        return 'rooftop'

class Rooftop(Level):
    """Escape Helicopter level"""
    def enter(self):
        print "=" * 80
        print "You step out onto the roof and see a flare gun on the ground. You pick it up and"
        print "fire off the flare into the sky. You see a helicopter approaching which fills you"
        print "with hope. The chopper hovers and drops a rope ladder for you to climb. You start"
        print "to move towards it but just as you are about to grab the ladder Godzilla bursts up"
        print "through the floor! You sprint as fast as you can and make a flying leap for the"
        print "ladder just as Godzilla's jaws snap shut just behind you. The helicopter flies away"
        print "while you climb the rest of the ladder. You collapse exhausted into the cabin and"
        print "shut your eyes knowing that you are safe."
        raw_input("'Enter'> ")
        print "=" * 80
        print "GAVE OVER YOU WIN!!"
        print "=" * 80
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
