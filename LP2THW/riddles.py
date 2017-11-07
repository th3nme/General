"""Riddles for RIDDicuLE Game"""
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
        print "You died"
    else:
        print "You win"

random_riddle()
