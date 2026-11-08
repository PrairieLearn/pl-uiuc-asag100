import random


def generate(data):
    slope = random.choice((-4, -3, -2, -1, 1, 2, 3, 4))
    turn_time = random.randint(2, 5)
    time_after_turn = random.randint(1, turn_time - 1)
    end_time = turn_time + time_after_turn
    intercept = -slope * turn_time

    linear_term = "t" if slope == 1 else "-t" if slope == -1 else f"{slope}t"
    sign = "+" if intercept > 0 else "-"
    data["params"].update({
        "velocity": f"{linear_term} {sign} {abs(intercept)}",
        "slope": slope,
        "intercept": intercept,
        "end_time": end_time,
        "initial_direction": "negative" if slope > 0 else "positive",
        "final_direction": "positive" if slope > 0 else "negative",
    })

    first_displacement = -slope * turn_time**2 / 2
    second_displacement = slope * time_after_turn**2 / 2
    data["correct_answers"].update({
        "turn_time": turn_time,
        "first_displacement": first_displacement,
        "second_displacement": second_displacement,
        "displacement": first_displacement + second_displacement,
        "distance": abs(first_displacement) + abs(second_displacement),
    })
