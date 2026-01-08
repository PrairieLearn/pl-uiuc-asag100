import random


def generate(data):
    stakes_pairs = {
        "high stakes": "will be included in a time exam that counts towards 35% of the overall grade",
        "low stakes": "will be included in a one homework that counts towards 1% of the overall grade",
    }
    explanation_pairs = {
        "no explanation": """
            The feedback states that the AI grader uses a hidden instructor-provided rubric to perform the grading:<br>
            Your grade is 50%, which was computed by the AI based on a rubric defined by the instructor, which will be available to you after the deadline""",
        "rubric information": """
            The feedback provides how the AI grader reaches its grading. 
            It includes an instructor-provided rubric used during the grading process, along with the weight of each rubric item:
            <ul style="list-style-type: none;"> 
                <li><i class="bi bi-check-square-fill" style="color: blue;"></i> which norm to use (50%) </li>
                <li><i class="bi bi-square"></i> error definition (25%)</li>
                <li><i class="bi bi-square"></i> interpretation of the norm magnitude in context (25%)</li>
            </ul>
        """,
        "improvement suggestions": """
            The feedback provides a list of things to consider/improve in order to receive a higher grade: 
            <ul> 
                <li>Draw connections between landscape changes and how we define numerical errors</li>
                <li>Incorporate the problem context more when stating the meaning of a large norm</li>
            </ul>
        """,
    }
    oversight_pairs = {
        "ai": "Given the latest technological advances and in an effort to perform grading in a timely manner for better learning outcomes, the AI grades will be final.",
        "human": "Given the latest technological advances and in an effort to provide feedback in a timely manner for better learning outcomes, the AI grader will provide a grade for reference, along with feedback for the student. A human TA will later manually check all the submissions and make a new grading while consulting the AI grades.",
    }
    resubmission_pairs = {
        "no": "Students can not modify the submission once submitted to the AI.",
        "yes": "Students can choose to modify the submission based on the feedback provided by the AI and resubmit to the AI for another round of grading.",
    }
    regrading_pairs = {
        "no": "Students can not choose to ask a TA for a regrade on the last submission.",
        "yes": "However, students can choose to ask a TA for a regrade on the last submission.",
    }

    stakes, stakes_text = random.choice(list(stakes_pairs.items()))
    explanation, explanation_text = random.choice(list(explanation_pairs.items()))
    oversight, oversight_text = random.choice(list(oversight_pairs.items()))
    resubmission, resubmission_text = random.choice(list(resubmission_pairs.items()))
    if oversight == "ai":
        regrading, regrading_text = random.choice(list(regrading_pairs.items()))
    else:
        regrading = "no"
        regrading_text = regrading_pairs[regrading]

    data["params"]["stakes_text"] = stakes_text
    data["params"]["oversight_text"] = oversight_text
    data["params"]["explanation_text"] = explanation_text
    data["params"]["resubmission_text"] = resubmission_text
    data["params"]["regrading_text"] = regrading_text

    data["params"]["stakes"] = stakes
    data["params"]["oversight"] = oversight
    data["params"]["explanation"] = explanation
    data["params"]["resubmission"] = resubmission
    data["params"]["regrading"] = regrading
