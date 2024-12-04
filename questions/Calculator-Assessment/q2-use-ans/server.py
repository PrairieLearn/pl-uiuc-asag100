import random
import math


def generate(data):
    deg = random.randint(70, 80)
    w = math.sin(deg * math.pi / 180)

    data["params"]["deg"] = deg
    data["correct_answers"]["w"] = w

    c1 = random.randint(5, 10)
    x = c1 * w
    data["params"]["c1"] = c1
    data["correct_answers"]["x"] = x

    c2 = random.randint(5, 10)
    y = x**2 - c2
    data["params"]["c2"] = c2
    data["correct_answers"]["y"] = y

    z = w * y
    data["correct_answers"]["z"] = z
