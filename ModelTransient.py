from random import randint
from Functiongenerator import get_function_1
from Functiongenerator import get_function_2

random_function = randint(0, 1)
random_observation = randint(0, 100)

if random_function == 0:
    magnitude = get_function_1()
if random_function == 1:
    magnitude = get_function_2(random_observation)


def make_observation():
    return magnitude

