import random


def generate(data):
    resistance_1, resistance_2 = random.sample(range(2, 7), 2)
    current = random.randint(1, 4)
    total_resistance = resistance_1 + resistance_2
    data["params"].update({
        "resistance_1": resistance_1,
        "resistance_2": resistance_2,
        "voltage": current * total_resistance,
    })
    data["correct_answers"].update({
        "total_resistance": total_resistance,
        "current": current,
        "voltage_1": current * resistance_1,
        "voltage_2": current * resistance_2,
    })
