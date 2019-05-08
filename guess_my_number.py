import random
my_number = random.randint(1,20)

game_over = False
number_of_guesses = 0

print("I'm thinking of a number between 1 and 20. What is it? You have 20 guesses.")

while not game_over:

    # get a new guess from the user
    answer = int(input("Guess a number: "))
    print("You guessed", answer )

    if answer == my_number:
        print("Congratulations, you guessed my number!")
        game_over = True
    else:
        print("Sorry, that's not it.")

    # add 1 to the number of guesses they have used, and end the game if they're out of guesses
    number_of_guesses = number_of_guesses + 1
    if number_of_guesses == 20:
        print("You're out of guesses.")
        game_over = True
