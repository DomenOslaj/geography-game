# A local gaming company contacted you to build a game for them. It is a simple geography quiz where a user has to guess the capital city of some country
import random

capital_city_dict = {"Austria": "Vienna", "Slovenia": "Ljubljana", "Italy": "Rome", "Germany": "Berlin",
                     "Croatia": "Zagreb", "Hungary": "Budapest"}

random_state = random.choice(list(capital_city_dict))

guess = input("Game: What is the capital city of {0}? \n".format(random_state))
print("User: {0}". format(guess))

while True:
    if capital_city_dict[random_state].lower() == guess.lower():
        print("Game: You are correct!")
        break
    elif capital_city_dict[random_state].lower() != guess.lower():
        print("Game: Wrong, try again. ")
        another_guess = input("Game: Another guess: ")
        if another_guess.lower() == capital_city_dict[random_state].lower:
            print("Game: Correct!")
            break
    else:
        print("Game: I dont understand you, try again.")
