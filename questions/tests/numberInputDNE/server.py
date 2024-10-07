import random
import sympy as sp


def generate(data):
    data["params"]["blank_value"] = 0xDEADBEEF

    a = 1
    b = random.randint(-1, 1)
    c = random.randint(-1, 1)
    data["params"]["a"] = a
    data["params"]["b"] = b
    data["params"]["c"] = c
    x = sp.var("x")

    f = a * x**2 + b * x + c
    data["params"]["function"] = f"{sp.latex(f)}=0"


def grade(data):
    a = data["params"]["a"]
    b = data["params"]["b"]
    c = data["params"]["c"]
    x = data["submitted_answers"]["x"]

    blank_value = data["params"]["blank_value"]

    det = b**2 - 4 * a * c
    if det < 0:
        if x == blank_value:
            data["partial_scores"]["x"] = {"score": 1}
        else:
            data["partial_scores"]["x"] = {"score": 0}
    else:
        f = a * x**2 + b * x + c
        if abs(f) <= 1e-12:
            data["partial_scores"]["x"] = {"score": 1}
        else:
            data["partial_scores"]["x"] = {"score": 0}
