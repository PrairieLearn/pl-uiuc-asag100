import random
from fractions import Fraction


def _cartesian_vector(components):
    terms = []
    for component, axis in zip(components, ("i", "j", "k")):
        value = Fraction(component)
        if value == 0:
            continue

        magnitude = abs(value)
        if magnitude.denominator == 1:
            coefficient = str(magnitude.numerator)
        else:
            coefficient = (
                f"\\frac{{{magnitude.numerator}}}{{{magnitude.denominator}}}"
            )

        sign = "-" if value < 0 else "+"
        if not terms:
            sign = "-" if value < 0 else ""
        terms.append(f"{sign}{coefficient}\\,\\hat{{\\mathbf{{{axis}}}}}")

    return " ".join(terms) if terms else r"\mathbf{0}"


def generate(data):
    nonzero_components = [value for value in range(-9, 10) if value != 0]
    a = [random.choice(nonzero_components) for _ in range(3)]
    b = [random.choice(nonzero_components) for _ in range(3)]
    a_dot_b = sum(ai * bi for ai, bi in zip(a, b))
    b_dot_b = sum(bi * bi for bi in b)
    scale = Fraction(a_dot_b, b_dot_b)
    c = [scale * bi for bi in b]

    data["params"]["a_vec"] = _cartesian_vector(a)
    data["params"]["b_vec"] = _cartesian_vector(b)
    data["params"]["a"] = a
    data["params"]["b"] = b
    for name, component in zip(("cx", "cy", "cz"), c):
        data["correct_answers"][name] = float(component)

    data["correct_answers"]["a_dot_b"] = a_dot_b
    data["correct_answers"]["b_dot_b"] = b_dot_b
    data["correct_answers"]["c_vec"] = _cartesian_vector(c)

    return data
