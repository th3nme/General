"""Riddles"""
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
    }

    error_count = 0
    while error_count < 3:
        # Get a random riddle and answer from riddles
        question = random.choice(list(riddles.keys()))
        correct_answer = riddles.get(question)
        print "=" * 60
        print "[Riddle]: %s" % question
        answer = raw_input("[Answer]: ")
        if answer.lower() == correct_answer.lower():
            print "correct"
        else:
            error_count += 1
            print "That answer is not correct"
    print "dead"

random_riddle()
