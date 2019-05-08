# game instructions
print("This is Mad Libs!")
print("Come up with words to fill in the blanks in a story.")
print()

# have the user come up with words to fill in the blanks
your_noun = input("Noun: ")
your_adj = input("Adjective: ")
your_verb = input("Verb: ")

# remind the user what they picked
print("Your noun is ", your_noun)
print("Your adjective is ", your_adj)
print("Your verb is ", your_verb)
print()

# show the story with the blanks filled in
print("Here's your story:")
print("Today, I tried to make cupcakes.")
print("I mixed the ingredients and put them in the", your_noun)
print("But it was too", your_adj, "!")
print("All I could do is", your_verb)