import random


def generate(data):
    stakes_pairs = {
        "high stakes": "on a final exam that counts towards 35% of the overall course grade",
        "low stakes": "on a homework assignment that counts towards 1% of the overall course grade",
    }
    explanation_pairs = {
        # "no explanation": """
        #     The feedback states that the AI grader assigns a score using an instructor-defined rubric that is not shown to students.<br>
        #     Your grade is 50%, which was computed by the AI based on a rubric defined by the instructor. The rubric will be available after the deadline.""",
        "rubric information": """
            <b>The feedback explains how the AI grader evaluated the response by listing the rubric items and their weights</b>:
            <ul style="list-style-type: none;"> 
                <li><i class="bi bi-check-square-fill" style="color: blue;"></i> list too short (50%) </li>
                <li><i class="bi bi-square"></i> negative numbers in the list (50%)</li>
                <li><i class="bi bi-square"></i> modify list in place (50%)</li>
            </ul>
        """,
        "improvement suggestions": """
            <b>The feedback includes specific suggestions for how the response could be improved to receive a higher score, such as</b>: 
            <ul> 
                <li>Consider how the result may change when negative numbers are involved</li>
                <li>Discuss the potential consequences of altering the original input list</li>
            </ul>
        """,
    }
    resubmission_pairs = {
        "no": "Students have only one opportunity to submit their response. After receiving AI feedback, they cannot modify or resubmit their answer.",
        "yes": "Students may revise their responses based on the AI feedback and resubmit multiple times for additional rounds of AI grading.",
    }
    # oversight_pairs = {
    #     "no": "The AI-assigned grade will not be manually reviewed by a human TA.",
    #     "yes": "The AI-assigned grade will later be reviewed by a human TA and adjusted if necessary.",
    # }
    # regrading_pairs = {
    #     "no": "	Students cannot request a regrade, and the AI-assigned score cannot be disputed.",
    #     "yes": "After the assessment closes, students have one week to request a regrade by a human TA if they believe the AI-assigned score is inaccurate.",
    # }
    ta_involvement_pairs = {
        "no": "The AI-assigned grade will not be manually reviewed by a human TA.",
        "review": "The AI-assigned grade will later be reviewed by a human TA and adjusted if necessary.",
        "regrade": "After the assessment closes, students have one week to request a regrade by a human TA if they believe the AI-assigned score is inaccurate."
    }

    stakes, stakes_text = random.choice(list(stakes_pairs.items()))
    explanation, explanation_text = random.choice(list(explanation_pairs.items()))
    resubmission, resubmission_text = random.choice(list(resubmission_pairs.items()))
    # oversight, oversight_text = random.choices(list(oversight_pairs.items()), weights = [2, 1])[0]
    # if oversight == "no":
    #     regrading, regrading_text = random.choice(list(regrading_pairs.items()))
    # else:
    #     regrading = "no"
    #     regrading_text = regrading_pairs[regrading]
    ta_involvement, ta_involvement_text = random.choice(list(ta_involvement_pairs.items()))

    data["params"]["stakes_text"] = stakes_text
    # data["params"]["oversight_text"] = oversight_text
    data["params"]["explanation_text"] = explanation_text
    data["params"]["resubmission_text"] = resubmission_text
    # data["params"]["regrading_text"] = regrading_text
    data["params"]["ta_involvement_text"] = ta_involvement_text

    data["params"]["stakes"] = stakes
    data["params"]["explanation"] = explanation
    data["params"]["resubmission"] = resubmission
    if ta_involvement == "no":
        data["params"]["oversight"] = "no"
        data["params"]["regrading"] = "no"
    elif ta_involvement == "review":
        data["params"]["oversight"] = "yes"
        data["params"]["regrading"] = "no"
    else:
        data["params"]["oversight"] = "no"
        data["params"]["regrading"] = "yes"
    


def grade(data):
    data["score"] = 1

    for num in range(11):
        data["partial_scores"][f"q{num}"] = {"score": None}
