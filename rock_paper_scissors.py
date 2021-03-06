# print game instructions
print("Let's play Rock, Paper, Scissors!")
print("Each win is worth 1 point. The first one to 5 points wins the game.")
print()

# reminder of what beats what
print("Remember:")
print("  paper beats rock")
print("  rock beats scissors")
print("  scissors beat paper")
print()

# initial set-up
import random
game_over = <put True or False here - which one should it be?>
player_score = 0
computer_score = 0

# main game loop
while not game_over:

    # get the player's choice

    player_choice = <get the player's input of rock, paper, or scissors>

    # use a random number to set the computer's choice

    number = <get a random number between 1 and 3>

    if number == 1:
        computer_choice = "rock"
    elif number == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    # compare the choices to decide the outcome for the player

    if player_choice == "rock":
        if computer_choice == "scissors":
            outcome = "win"
        elif computer_choice == "paper":
            outcome = "loss"
        else:
            outcome = "tie"

    elif player_choice == "paper":
        if computer_choice == "rock":
            outcome = "win"
        elif computer_choice == "scissors":
            outcome = "loss"
        else:
            outcome = "tie"

    elif player_choice == <put the last remaining possibility here>:
        if computer_choice == "paper":
            outcome = "win"
        elif computer_choice == "rock":
            outcome = "loss"
        else:
            outcome = "tie"

    else:
        outcome = "error"

    # print the outcome and update the scores

    if outcome == "win":
        <print a message telling the player they won>
        player_score = player_score + 1

    elif outcome == "loss":
        <print a message telling the player they lost>
        computer_score = computer_score + 1

    elif outcome == "tie":
        <print a message telling the player it's a tie>

    else:
        print("You must enter one of these choices: rock, paper, scissors")

    print("Player:", player_score)
    <print a similar message showing the computer's score>
    print()

    # stop when someone reaches 5 points
    if (player_score == 5) or (computer_score == 5):
        game_over = True

