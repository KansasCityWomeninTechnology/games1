import random

print("Welcome to Adventure Game! You will climb a mountain to reach the diamond at the top.")
print("To win this game, you must have")
print("  speed to escape the lion...")
print("  smarts to beat the troll...")
print("  and strength to push aside the rock.")
print("Once you have accomplished all of these, you get the diamond! Ready? Let's go!")
print()

lion_vanquished = False
troll_beaten = False
rock_moved = False
game_over = False

player_has_strength_spell = False
number_of_lives = 3
safe_lion_distance = 20

def roll_dice():
    input("Press Enter to roll the dice.")
    dice_result = random.randint(1,4)
    return dice_result

def encounter_lion():

    global lion_vanquished
    global number_of_lives

    if lion_vanquished:

        print("You're safe for now.")

    else:

        print("Oh no! You encounter a lion.")
        print("Keep pressing the space bar to run away. Press Enter when you think you're far enough.")
        player_spaces = input("~/-\o ROAR")
        player_distance = len(player_spaces)

        if player_distance >= safe_lion_distance:
            print("You were fast enough to escape the lion. Well done!")
            lion_vanquished = True
        else:
            print("Too slow, the lion ate you!")
            number_of_lives = number_of_lives - 1
            print("You have", number_of_lives, "lives left.")

    return

def encounter_troll():

    global troll_beaten
    global number_of_lives

    if troll_beaten:

        print("You're safe for now.")

    else:

        print("You see a troll. He says:")
        print("To get past me, you must answer my riddle correctly. Your life depends on it!")
        player_answer = input("What is my favorite color? ")

        if player_answer.lower() == "blue":
            print("You have outsmarted the troll. Good job!")
            troll_beaten = True
        else:
            print("Uh-oh, wrong answer!")
            number_of_lives = number_of_lives - 1
            print("You have", number_of_lives, "lives left.")

    return

def get_strength_spell():

    global player_has_strength_spell

    if player_has_strength_spell:
        print("You're safe for now.")
    else:
        player_has_strength_spell = True
        print("You now have a strength spell. This will give you extra strength.")
    return

def encounter_rock():

    global player_has_strength_spell
    global rock_moved
    global number_of_lives

    if rock_moved:

        print("You're safe for now.")

    else:

        print("A huge rock comes rolling down the mountain at you! You need to push it aside so it doesn't smash you.")

        if player_has_strength_spell:
            print("Fortunately, you have the strength spell.")
            print("Congratulations! Your strength allowed you to push aside the rock.")
            rock_moved = True
        else:
            print("Oh no! You couldn't push aside the rock - it rolled right over you.")
            number_of_lives = number_of_lives - 1
            print("You have", number_of_lives, "lives left.")

    return

# main game loop
while not game_over:

    dice_result = roll_dice()
    print("You rolled a", dice_result)

    if dice_result == 1:
        encounter_lion()
    elif dice_result == 2:
        encounter_troll()
    elif dice_result == 3:
        get_strength_spell()
    elif dice_result == 4:
        encounter_rock()

    # add a blank line
    print()

    if number_of_lives < 1:
        print("GAME OVER")
        game_over = True
    elif lion_vanquished and troll_beaten and rock_moved:
        print("You have overcome all the obstacles. The diamond is yours!")
        print("**********************************************************")
        game_over = True
    else:
        print("Continue your journey.")

    # add a blank line before the next turn
    print()
