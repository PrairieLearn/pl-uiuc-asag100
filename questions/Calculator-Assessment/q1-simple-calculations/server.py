import random
import math


def generate(data):
    a = round(random.random() * 10 + 10, 2)
    b = round(random.random() * 10 + 10, 2)
    z = a * b
    data["params"]["a"] = a
    data["params"]["b"] = b
    data["correct_answers"]["z"] = z

    c = random.randint(30, 50)
    d = random.randint(80, 100)
    y = c / d
    data["params"]["c"] = c
    data["params"]["d"] = d
    data["correct_answers"]["y"] = y

    e = random.randint(2, 5)
    x = math.e**e
    data["params"]["e"] = e
    data["correct_answers"]["x"] = x
