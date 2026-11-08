import random


def generate(data):
    offset = random.choice((0, 1))
    data["params"]["expression"] = "n(n+1)" if offset == 0 else "n(n+1)+1"
    data["params"]["parity"] = "even" if offset == 0 else "odd"
    data["params"]["odd_version"] = offset == 1
    data["correct_answers"]["offset"] = offset
