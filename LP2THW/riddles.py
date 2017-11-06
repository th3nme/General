import random

def random_riddle():
    
    riddles = {
        "Poor people have it, Rich People need it. If you eat it you die.":
            "nothing",
        "Mary's father has 5 daughters. Nana, Nene, Nini, Nono and ..."
        "What is the fifth daughters name?":
            "mary",
        "How can a pants pocket be empty and still have something in it?":
            "hole",
        "What word becomes shorter when you add two letters to it?":
            "short",
        "If I have it, I haven't shared it. If I share it, I don't have it anymore.":
            "secret",
    }

    question = random.choice(list(riddles.keys()))
    correct_answer = riddles.get(question)
    error_count = 0
    print "=" * 60
    print "[Riddle]: %s" % question
    answer = raw_input("[Answer]: ")
    if answer.lower() == correct_answer.lower():
        print "correct"
    else:
        error_count += 1
        print "wrong"

random_riddle()