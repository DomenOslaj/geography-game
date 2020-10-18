# A local gaming company contacted you to build a game for them. It is a simple geography quiz where a user has to guess the capital city of some country
import random

capital_city_dict = {"Austria": "Vienna", "Slovenia": "Ljubljana", "Italy": "Rome", "Germany": "Berlin",
                     "Croatia": "Zagreb", "Hungary": "Budapest"}

random_state = random.choice(list(capital_city_dict))

print(random_state)