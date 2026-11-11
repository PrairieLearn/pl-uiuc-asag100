import random
from fractions import Fraction


RUBRIC_ITEMS = (
    {
        "number": 1,
        "description": "Correct formula for projection",
        "guidance": (
            r"Write a correct symbolic formula for projecting $\vec{a}$ onto $\vec{b}$. "
            r"Accept equivalent forms such as $(\vec{a}\cdot\hat{b})\hat{b}$."
        ),
    },
    {
        "number": 2,
        "description": "Correct intermediate computations",
        "guidance": (
            "Carry out the computations needed for your chosen formula. "
            "Correct work for an incorrect formula can earn this item, and a "
            "minor arithmetic slip still earns it if the work is generally correct."
        ),
    },
    {
        "number": 3,
        "description": "Correct final answer",
        "guidance": (
            "Give a vector in any standard notation. A vector computed correctly "
            "from your stated formula and intermediate results also earns this item "
            "if the earlier work contains an error."
        ),
    },
)

# Final credit depends on how the work is carried through.
RUBRIC_PROFILES = {
    "correct": (1, 2, 3),
    # Correct formula and intermediate values, but reports the scale as the answer.
    "scalar_answer": (1, 2),
    # Writes the correct formula, then substitutes the norm for its square and follows through.
    "wrong_intermediate": (1, 3),
    # Substitutes the norm for its square and reports only the scale.
    "wrong_intermediate_and_scalar_answer": (1,),
    # Writes the formula for projection onto a and evaluates that formula correctly.
    "wrong_formula": (2, 3),
    # Uses the wrong formula, computes its intermediate values, and reports only the scale.
    "wrong_formula_and_scalar_answer": (2,),
    # Projects onto a, leaves out a term of the dot product, and correctly scales a.
    "wrong_formula_and_intermediate": (3,),
}


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
    c_vec = _cartesian_vector(c)
    data["correct_answers"]["c_vec"] = c_vec

    handwriting_quality = random.choice(("neat", "messy"))
    solution_organization = random.choice(("organized", "disorganized"))
    profile = data.get("preferences", {}).get("rubric_profile", "random")
    if profile == "random":
        profile = "correct"
        if random.choice((False, True)):
            partial_profiles = tuple(name for name in RUBRIC_PROFILES if name != "correct")
            profile = random.choice(partial_profiles)
    if profile not in RUBRIC_PROFILES:
        raise ValueError(f"Unknown rubric profile: {profile}")

    selected = RUBRIC_PROFILES[profile]
    references = {
        1: r"\vec{c}=\frac{\vec{a}\cdot\vec{b}}{\vec{b}\cdot\vec{b}}\,\vec{b}",
        2: (
            rf"\vec{{a}}\cdot\vec{{b}}={a_dot_b}\,\mathrm{{m}}^2,\quad "
            rf"\vec{{b}}\cdot\vec{{b}}={b_dot_b}\,\mathrm{{m}}^2"
        ),
        3: rf"\vec{{c}}={c_vec}\,\mathrm{{m}}",
    }
    rubric_targets = [
        {
            **item,
            "checked": item["number"] in selected,
            "reference_latex": references[item["number"]],
        }
        for item in RUBRIC_ITEMS
    ]
    data["params"].update({
        "a_dot_b_work": " + ".join(f"({ai})({bi})" for ai, bi in zip(a, b)),
        "b_dot_b_work": " + ".join(f"({bi})^2" for bi in b),
        "handwriting_quality": handwriting_quality,
        "solution_organization": solution_organization,
        "is_messy": handwriting_quality == "messy",
        "is_disorganized": solution_organization == "disorganized",
        "rubric_profile": profile,
        "submission_correctness": "correct" if profile == "correct" else "partially correct",
        "rubric_targets": rubric_targets,
        "rubric_met_count": len(selected),
        "rubric_math_count": len(RUBRIC_ITEMS),
    })

    return data
