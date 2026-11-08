import os
import random


RUBRIC_ITEMS = (
    {
        "number": 1,
        "description": "Reasonable attempt at a free-body diagram",
        "guidance": "A reasonable attempt earns this item even if the diagram is incomplete or inaccurate. A complete, correct free-body diagram also satisfies this item.",
    },
    {
        "number": 2,
        "description": "Correct free-body diagram",
        "guidance": "Includes the applied distributed load and couple moment, plus the reaction force and reaction moment at x=0. Applied-load directions must match the given image. Assumed reaction directions may be arbitrary.",
    },
    {
        "number": 3,
        "description": "Attempts to sum forces in the y direction",
        "guidance": "Shows an attempt to write a vertical force balance. Award this item even if the equation or subsequent calculation is incorrect.",
    },
    {
        "number": 4,
        "description": "Attempts to sum moments about a point",
        "guidance": "Shows an attempt to write a moment balance about any point. Award this item even if the equation or subsequent calculation is incorrect.",
    },
    {
        "number": 5,
        "description": "Correct reaction force magnitude",
        "guidance": "The reaction force magnitude matches the reference value. Either assumed reaction direction is acceptable. Assess this result independently of the equilibrium-attempt items.",
    },
    {
        "number": 6,
        "description": "Correct reaction moment magnitude",
        "guidance": "The reaction moment magnitude matches the reference value. Either assumed reaction direction is acceptable. Assess this result independently of the equilibrium-attempt items.",
    },
)

RUBRIC_PROFILES = {
    "correct": (1, 2, 3, 4, 5, 6),
    "partial_1": (1, 3, 5),
    "partial_2": (1, 2, 3, 5),
    "partial_3": (1, 2, 3, 4),
    "partial_4": (1, 2, 3, 4, 5),
}


def _rubric_targets(profile):
    if profile not in RUBRIC_PROFILES:
        raise ValueError(f"Unknown rubric profile: {profile}")
    selected = RUBRIC_PROFILES[profile]
    return [item["number"] in selected for item in RUBRIC_ITEMS]


def file(data):
    if data["filename"] == "figure.png":
        image_name = data["params"]["selected_image"]

        image_path = os.path.join(
            "clientFilesQuestion",
            image_name,
        )

        with open(image_path, "rb") as f:
            return f.read()


def generate(data):
    w = random.randint(4, 10)
    a = random.randint(3, 4)
    mo = random.randint(4, 8)

    data["params"]["w"] = w
    data["params"]["a"] = a
    data["params"]["mo"] = mo

    problem_choice = random.choice([1, 2, 3])

    if problem_choice == 1:
        R = w * a
        Ma = 3 * w * a * a / 2 + mo
        image = "Picture3.png"
    elif problem_choice == 2:
        R = w * a
        Ma = w * a * a / 2 + mo
        image = "Picture4.png"
    else:
        R = w * a
        Ma = 5 * w * a * a / 2 - mo
        image = "Picture5.png"

    data["params"]["selected_image"] = image
    data["params"]["R"] = R
    data["params"]["Ma"] = Ma

    centroid_factors = {1: 1.5, 2: 0.5, 3: 2.5}
    centroid_symbols = {1: r"\frac{3a}{2}", 2: r"\frac{a}{2}", 3: r"\frac{5a}{2}"}
    load_intervals = {1: "a to 2a", 2: "0 to a", 3: "2a to 3a"}
    clockwise = problem_choice != 3
    params = data["params"]
    params.update({
        "problem_choice": problem_choice,
        "load_centroid": centroid_factors[problem_choice] * a,
        "load_centroid_latex": f"{centroid_factors[problem_choice] * a:g}",
        "load_centroid_symbol": centroid_symbols[problem_choice],
        "load_interval": load_intervals[problem_choice],
        "applied_moment_direction": "clockwise" if clockwise else "counterclockwise",
        "moment_balance_sign": "-" if clockwise else "+",
        "reaction_moment_sign": "+" if clockwise else "-",
        "moment_magnitude_latex": f"{abs(Ma):g}",
        "reference_image": f"FBD{problem_choice + 2}.svg",
        "handwriting_quality": random.choice(("neat", "messy")),
        "solution_organization": random.choice(("organized", "disorganized")),
    })
    params["is_messy"] = params["handwriting_quality"] == "messy"
    params["is_disorganized"] = params["solution_organization"] == "disorganized"

    profile = data.get("preferences", {}).get("rubric_profile", "random")
    if profile == "random":
        correctness = random.choice(("correct", "partially correct"))
        profile = "correct" if correctness == "correct" else random.choice((
            "partial_1", "partial_2", "partial_3", "partial_4"
        ))
    targets = _rubric_targets(profile)
    params["rubric_profile"] = profile
    params["submission_correctness"] = "correct" if profile == "correct" else "partially correct"
    references = {
        5: rf"|R_y|={R}\,\mathrm{{kN}}",
        6: rf"|M_A|={params['moment_magnitude_latex']}\,\mathrm{{kN\,m}}",
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
