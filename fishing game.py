# Copyright (c) 2019 kris reynolds(renfield101@hotmail.com)
# A Text Based Fishing Game

import time
import random
import shelve
from sys import exit

# Initialize the PRNG
random.seed()

# The scorefile is kept as a dictionary mapping
# username to score, stored in a "shelf".
user_scores = shelve.open("fishing")

def register(username):
    "Register a new, legal username."
    for c in username:
        if not (c.isalpha() or c.isdigit() or c in "_-"):
            print("illegal character in username " + \
                  "(legal are A-Za-z0-9_-)")
            return
    if username in user_scores:
        print("username already registered")
        return
    user_scores[username] = 0
    user_scores.sync()

# The username of the current fisher
fisher = None

def fish(username):
    "Set the fisher to an existing username."
    global fisher
    if not (username in user_scores):
        print("username unknown")
        return
    fisher = username

def fisher_score():
    global fisher
    print("Your current score is " + str(user_scores[fisher]))

# Dictionary of fishes keyed by fish and contents
# a two-tuple indicating the percent probability and
# the score of that fish.
fishes = (
    (None, 20, 5),
    ("Roach - 1.5 lbs with white maggot", 20, 10),
    ("Chub - 3.6 lbs with a slug", 30, 30),
    ("Common Carp - 9.8 lbs with boilies", 10, 100),
    ("Boss Mirror carp - 17 lbs with bread", 5, 200),
    ("Boss Tench - 7.3 lbs with red worm", 1, 5000), )

def cast_result():
    """
    Get the result of a cast. Returns a tuple of fish
    description and cast score.
    """
    catch = random.randrange(100)
    for (fish, percent, score) in fishes:
        catch -= percent
        if catch < 0:
            return (fish, score)
    assert False

def fish_name(fish):
    "Return canonical name of a fish."
    if fish == None:
        return "An Old Boot"
    return " " + fish

def cast():
    time.sleep(2)
    print("<><" " You cast your float into the water.")
    time.sleep(1)
    print("<><" ' *')
    time.sleep(1)
    print("<><" ' **')
    time.sleep(1)
    print("<><" ' ***')
    time.sleep(2)
    groundbait = input("<><" " Do you wanna use ground bait? ")
    if 'yes' in groundbait:
            if 'y' in groundbait:
              if 'yh' in groundbait:
                if 'yeah' in groundbait:
                    time.sleep(1)
    print("<><" ' ****')
    time.sleep(2)
    print("<><" " ***** Five mins go by!")
    time.sleep(1)
    print("<><" ' ******')
    time.sleep(1)
    print("<><" ' *******')
    time.sleep(1)
    print("<><" ' ********')
    time.sleep(1)
    print("<><" ' *********')
    time.sleep(2)
    print("<><" " *********** Ten mins go by!")
    time.sleep(2)
    print("<><" " You see the float dip sightly, Wait Stay Quiet! ")
    time.sleep(2)
    strike = input("<><" " Do you want to strike? ")
    if 'yes' in strike:
        if 'y' in strike:
            if 'yh' in strike:
                if 'yeah' in strike:
                    global fisher
    if fisher == None:
        print('Use the "fish" command to choose a fisher.')
        return
    (fish, score) = cast_result()
    time.sleep(2)
    print("<>< Fish on! ")
    time.sleep(2)
    print("<><" " You have Landed ", end="")
    if fish == None:
        time.sleep(2)
        print(fish_name(fish) + ".")
        return
    time.sleep(2)
    print("a " + fish_name(fish) + "!")
    time.sleep(2)
    print("It is worth " + str(score) + " points. well done old chap! Type cast to try your luck again!")
    time.sleep(2)
    user_scores[fisher] += score
    user_scores.sync()
    fisher_score()

def scores():
    "Show everyone's score."
    global fisher
    if fisher != None:
        fisher_score()
        print("")
    print("All scores:")
    for u in user_scores:
        print(u + ": " + str(user_scores[u]))

def quit():
    "Quit the game."
    scores()
    user_scores.close()
    exit()

def help():
    "Show help."
    print("""
    register <username>: Register a new fisher named username
    fish <username>: Start username fishing
    cast: Try to catch a fish
    scores: Find out everyone's score
    quit: Quit the game
    help: This help
    yes,yeah,y,yh: Are all acepted answers
    """)

def test():
    "Test the fishing algorithm."
    counts = {}
    for (fish, _, _) in fishes:
        counts[fish] = 0
    for i in range(1000000):
        (fish, _) = cast_result()
        counts[fish] += 1
    for fish in counts:
        print(fish_name(fish) + ": " + str(counts[fish]))

# Fishing commands. Each command comes with its argument
# count and its function.
commands = { "register" : (1, register),
             "fish" : (1, fish),
             "cast" : (0, cast),
             "scores" : (0, scores),
             "quit" : (0, quit),
             "help" : (0, help),
             "test" : (0, test) }

# The main loop
print('Fishing! Please enter fishing commands. "help" for help.')
while True:
    words = []
    while words == []:
        try:
            cmd = input("<>< ")
        except EOFError:
            print("quit")
            cmd = "quit"
        words = cmd.split()
    if words[0] in commands:
        (nargs, cmd_fun) = commands[words[0]]
        if len(words) - 1 != nargs:
            print("Wrong number of arguments to command. Please try again")
            continue
        if nargs == 0:
            cmd_fun()
        elif nargs == 1:
            cmd_fun(words[1])
        else:
            assert False
        continue
    print("Unknown fishing command. Please try again or type help.")
