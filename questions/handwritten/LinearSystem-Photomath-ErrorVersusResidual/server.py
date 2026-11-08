import random
import numpy as np
import math
from fractions import Fraction


RUBRIC_ITEMS = (
    {
        "number": 1,
        "description": "Correct solution for x",
        "guidance": "Both coordinates have the correct values and signs. Accept exact fractions or decimals accurate to at least three significant figures. Treat 0 and -0 as identical.",
    },
    {
        "number": 2,
        "description": "Correct setup to compute the error",
        "guidance": "Sets up the subtraction correctly. Give setup credit even if the solution vector carried forward from item 1 is incorrect; assess the numerical result separately in item 3.",
    },
    {
        "number": 3,
        "description": "Correct calculation for the error",
        "guidance": "Matches the displayed reference error vector. Accept exact fractions or decimals accurate to at least three significant figures. Treat 0 and -0 as identical.",
    },
    {
        "number": 4,
        "description": "Correct setup to compute the residual",
        "guidance": "Sets up the matrix-vector multiplication and subtraction correctly. Give setup credit even if an incorrect vector from item 1 is carried forward; assess the numerical result separately in item 5. The reference setup uses the supplied approximate solution.",
    },
    {
        "number": 5,
        "description": "Correct calculation for the residual",
        "guidance": "Matches the displayed reference residual vector. Accept exact fractions or decimals accurate to at least three significant figures. Treat 0 and -0 as identical.",
    },
    {
        "number": 6,
        "description": "Selects residual as the stopping criterion",
        "guidance": "States that the residual should be used to decide when to stop the iterative solver.",
    },
    {
        "number": 7,
        "description": "Correct explanation",
        "guidance": "Explains that the true solution, and therefore the error, is not known during the iterative process, whereas the residual can be computed from the known data and the current approximation.",
    },
)

# Only these predefined assignments are allowed.
RUBRIC_PROFILES = {
    "correct": (1, 2, 3, 4, 5, 6, 7),
    "partial_1": (1, 2, 3, 5, 6),
    "partial_2": (1, 2, 3),
    "partial_3": (1, 3, 4, 5, 6),
    "partial_4": (1, 3, 4),
    "partial_5": (2, 4, 6, 7),
}


def _rubric_targets(profile):
    if profile not in RUBRIC_PROFILES:
        raise ValueError(f"Unknown rubric profile: {profile}")
    selected = RUBRIC_PROFILES[profile]
    return [item["number"] in selected for item in RUBRIC_ITEMS]


def _latex_fraction(value):
    if value.denominator == 1:
        return str(value.numerator)
    sign = "-" if value < 0 else ""
    return f"{sign}\\frac{{{abs(value.numerator)}}}{{{value.denominator}}}"


def _latex_vector(values):
    entries = r"\\".join(_latex_fraction(Fraction(value)) for value in values)
    return rf"\begin{{pmatrix}}{entries}\end{{pmatrix}}"


def generate(data):

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    l1 = random.randint(1, 10)
    l2 = random.randint(1, 10)
    
    den = b*c - a*d

    if (den == 0):
        return generate(data)
    
    xnum = b * l2 - d * l1
    ynum = l1 * c - a * l2

    data["params"]["arep"] = f"\\begin{{pmatrix}}{a} & {b}\\\\ {c} & {d}\\end{{pmatrix}}"
    data["params"]["brep"] = f"\\begin{{pmatrix}}{l1}\\\\{l2}\\end{{pmatrix}}"



    data["params"]["xrep"] = f"\\begin{{pmatrix}}\\frac{{{xnum // math.gcd(xnum, den)}}}{{{den // math.gcd(xnum, den)}}}\\\\ \\frac{{{ynum // math.gcd(ynum, den)}}}{{{den // math.gcd(ynum, den)}}}\\end{{pmatrix}}"

    estx = round(xnum/den)
    esty = round(ynum/den)

    data["params"]["estrep"] = f"\\begin{{pmatrix}}{estx}\\\\{esty}\\end{{pmatrix}}"
    data["params"]["errrep"] = f"\\begin{{pmatrix}}\\frac{{{-(estx * den - xnum) // math.gcd((estx * den - xnum), den)}}}{{{den // math.gcd((estx * den - xnum), den)}}}\\\\ \\frac{{{-(esty * den - ynum) // math.gcd((esty * den - ynum), den)}}}{{{den // math.gcd((esty * den - ynum), den)}}}\\end{{pmatrix}}"
    data["params"]["resrep"] = f"\\begin{{pmatrix}}{-(a * estx + b * esty - l1)}\\\\{-(c * estx + d * esty - l2)}\\end{{pmatrix}}"
    data["params"]["negerrrep"] = f"\\begin{{pmatrix}}\\frac{{{(estx * den - xnum) // math.gcd((estx * den - xnum), den)}}}{{{den // math.gcd((estx * den - xnum), den)}}}\\\\ \\frac{{{(esty * den - ynum) // math.gcd((esty * den - ynum), den)}}}{{{den // math.gcd((esty * den - ynum), den)}}}\\end{{pmatrix}}"
    data["params"]["negresrep"] = f"\\begin{{pmatrix}}{a * estx + b * esty - l1}\\\\{c * estx + d * esty - l2}\\end{{pmatrix}}"

    if (np.linalg.norm(np.array([(estx * den - xnum)/den, (esty * den - ynum)/den])) >= np.linalg.norm([a * estx + b * esty - l1, c * estx + d * esty - l2])):
        return generate(data)

    solution = (Fraction(xnum, den), Fraction(ynum, den))
    error = (solution[0] - estx, solution[1] - esty)
    data["params"].update({
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "rhs1": l1,
        "rhs2": l2,
        "determinant": a * d - b * c,
        "solution_x1": _latex_fraction(solution[0]),
        "solution_x2": _latex_fraction(solution[1]),
        "solution_vector": _latex_vector(solution),
        "product_vector": _latex_vector((a * estx + b * esty, c * estx + d * esty)),
        "error_vector": _latex_vector(error),
        "estimate_x1": estx,
        "estimate_x2": esty,
        "handwriting_quality": random.choice(("neat", "messy")),
        "solution_organization": random.choice(("organized", "disorganized")),
    })
    data["params"]["is_messy"] = data["params"]["handwriting_quality"] == "messy"
    data["params"]["is_disorganized"] = data["params"]["solution_organization"] == "disorganized"
    profile = data.get("preferences", {}).get("rubric_profile", "random")
    if profile == "random":
        correctness = random.choice(("correct", "partially correct"))
        profile = "correct" if correctness == "correct" else random.choice((
            "partial_1", "partial_2", "partial_3", "partial_4", "partial_5"
        ))
    targets = _rubric_targets(profile)
    params = data["params"]
    params["rubric_profile"] = profile
    params["submission_correctness"] = "correct" if profile == "correct" else "partially correct"
    references = {
        1: rf"\mathbf{{x}}={params['solution_vector']}",
        2: r"\mathbf{e}=\mathbf{x}-\hat{\mathbf{x}}",
        3: rf"\mathbf{{e}}={params['error_vector']}",
        4: r"\mathbf{r}=\mathbf{b}-\mathbf{A}\hat{\mathbf{x}}",
        5: rf"\mathbf{{r}}={params['resrep']}",
    }
    params["rubric_targets"] = [
        {
            **item,
            "checked": checked,
            "reference_latex": references.get(item["number"], ""),
        }
        for item, checked in zip(RUBRIC_ITEMS, targets)
    ]
    params["rubric_met_count"] = sum(targets)
    params["rubric_criterion_count"] = len(RUBRIC_ITEMS)
