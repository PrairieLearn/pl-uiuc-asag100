import random


RUBRIC_ITEMS = (
    {
        "number": 1,
        "description": "Correctly factors the cubic equation",
        "guidance": (
            "Writes the equation as a product of x and the correct quadratic "
            "set equal to zero, or shows an equivalent algebraic step."
        ),
    },
    {
        "number": 2,
        "description": "Identifies zero as a root",
        "guidance": (
            "Explicitly gives x = 0 as a root when applying the zero-product "
            "property or when listing the final roots."
        ),
    },
    {
        "number": 3,
        "description": "Correctly sets up the solution of the quadratic",
        "guidance": (
            "Substitutes the correct coefficients into the quadratic formula, "
            "or gives a valid setup for another method such as completing the "
            "square. Assess subsequent arithmetic under items 4 through 6."
        ),
    },
    {
        "number": 4,
        "description": "Correctly evaluates the discriminant",
        "guidance": (
            "Shows the correct numerical discriminant or the equivalent "
            "radicand from completing the square. Assess this calculation "
            "independently of the rest of the quadratic setup."
        ),
    },
    {
        "number": 5,
        "description": "Gives the correct positive root",
        "guidance": (
            "Accept an equivalent exact expression or a decimal correctly "
            "rounded to at least three significant figures."
        ),
    },
    {
        "number": 6,
        "description": "Gives the correct negative root",
        "guidance": (
            "Accept an equivalent exact expression or a decimal correctly "
            "rounded to at least three significant figures."
        ),
    },
)

# Each partial profile can arise from a single mistake.
RUBRIC_PROFILES = {
    "correct": (1, 2, 3, 4, 5, 6),
    # Keeps only the plus branch of the formula.
    "partial_1": (1, 2, 3, 4, 5),
    # Factors out x but reports only the quadratic roots.
    "partial_2": (1, 3, 4, 5, 6),
    # Substitutes correctly, then simplifies 2(5) to 5.
    "partial_3": (1, 2, 3, 4),
    # Substitutes correctly, then omits the 1 when adding the discriminant terms.
    "partial_4": (1, 2, 3),
    # Evaluates the discriminant correctly but uses b in place of -b in the numerator.
    "partial_5": (1, 2, 4),
}


def _rubric_targets(profile):
    if profile not in RUBRIC_PROFILES:
        raise ValueError(f"Unknown rubric profile: {profile}")
    selected = RUBRIC_PROFILES[profile]
    return [item["number"] in selected for item in RUBRIC_ITEMS]


def generate(data):
    c_magnitude = random.randint(1, 3)
    c = -c_magnitude
    discriminant = 1 + 20 * c_magnitude
    quadratic = rf"5x^2 - x - {c_magnitude}"
    factored_equation = rf"x\left({quadratic}\right)=0"
    quadratic_setup = rf"x=\frac{{-(-1)\pm\sqrt{{(-1)^2-4(5)({c})}}}}{{2(5)}}"
    root_plus = rf"\frac{{1+\sqrt{{{discriminant}}}}}{{10}}"
    root_minus = rf"\frac{{1-\sqrt{{{discriminant}}}}}{{10}}"

    handwriting_quality = random.choice(("neat", "messy"))
    solution_organization = random.choice(("organized", "disorganized"))
    profile = data.get("preferences", {}).get("rubric_profile", "random")
    if profile == "random":
        correctness = random.choice(("correct", "partially correct"))
        partial_profiles = tuple(name for name in RUBRIC_PROFILES if name != "correct")
        profile = "correct" if correctness == "correct" else random.choice(partial_profiles)

    targets = _rubric_targets(profile)
    references = {
        1: factored_equation,
        2: r"x=0",
        3: quadratic_setup,
        4: rf"\Delta=(-1)^2-4(5)({c})={discriminant}",
        5: rf"x={root_plus}",
        6: rf"x={root_minus}",
    }
    data["params"].update({
        "f": rf"5x^3 - x^2 - {c_magnitude}x",
        "D": discriminant,
        "c": c,
        "quadratic": quadratic,
        "factored_equation": factored_equation,
        "quadratic_setup": quadratic_setup,
        "root_plus": root_plus,
        "root_minus": root_minus,
        "handwriting_quality": handwriting_quality,
        "solution_organization": solution_organization,
        "is_messy": handwriting_quality == "messy",
        "is_disorganized": solution_organization == "disorganized",
        "rubric_profile": profile,
        "submission_correctness": "correct" if profile == "correct" else "partially correct",
        "rubric_targets": [
            {**item, "checked": checked, "reference_latex": references[item["number"]]}
            for item, checked in zip(RUBRIC_ITEMS, targets)
        ],
        "rubric_met_count": sum(targets),
        "rubric_criterion_count": len(RUBRIC_ITEMS),
    })
