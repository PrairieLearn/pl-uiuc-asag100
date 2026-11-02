import math
import random
import numpy as np
import prairielearn as pl


def generate(data):
    # Sample a random decimal number in the tenths place between 1.1 and 5
    a = random.randint(1, 5)

    # Sample an integer number between 6 and 11
    b = random.randint(6, 10)

    data["params"]["a"] = a
    data["params"]["b"] = b

    c = random.choice(["Hi", "Hello", "Good morning"])
    data['params']['c'] = c

def grade(data):
    a = data['submitted_answers']['a']
    if np.isclose(a, data['params']['a']):
        score_a = 1
    else:
        score_a = 0

    b = data['submitted_answers']['b']
    if np.isclose(b, data['params']['b']):
        score_b = 1
    else:
        score_b = 0

    c = data['submitted_answers']['c']
    if c == data['params']['c']:
        score_c = 1
    else:
        score_c = 0

    data["partial_scores"]["a"] = {"score": score_a, "weight": 1}
    data["partial_scores"]["b"] = {"score": score_b, "weight": 1}
    data["partial_scores"]["c"] = {"score": score_c, "weight": 3}

    pl.set_weighted_score_data(data)

