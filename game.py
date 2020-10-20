# A local gaming company contacted you to build a game for them. It is a simple geography quiz where a user has to
# guess the capital city of some country
import random

capital_city_dict = {"Austria": "Vienna", "Slovenia": "Ljubljana", "Italy": "Rome", "Germany": "Berlin",
                     "Croatia": "Zagreb", "Hungary": "Budapest"}


# ask user for  capital city of that state
def user_guess():
    guess = input("Game: What is the capital city of {0}? \n".format(random_state))
    print("User: {0}". format(guess))
    return guess.lower()


# play game
def play_game(guess):
    while True:
        if capital_city_dict[random_state].lower() == guess():
            print("Game: You are correct!")
            break
        else:
            print("Game: Not correct, try again.")


# opening selection
while True:
    # chose random state
    random_state = random.choice(list(capital_city_dict))

    selection = input("Would you like to A) play a game, B) exit: ")
    if selection.lower() == "a":
        play_game(user_guess)
    elif selection.lower() == "b":
        break
    else:
        print("Only A) and B) possibilities to choose from!")

