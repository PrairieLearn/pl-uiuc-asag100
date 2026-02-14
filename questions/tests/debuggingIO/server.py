import random
import json


def customSum(lst):
    return sum(lst)


def assignScore(data, i, score):
    data["partial_scores"][f"row-{i}-input"] = {"score": score, "weight": 0.5}
    data["partial_scores"][f"row-{i}-length"] = {"score": score, "weight": 0.5}


def generate(data):

    i = 0
    row_fill_input = random.choice([True, False])
    data["params"][f"row-{i}-fill-input"] = row_fill_input

    row_input = [1, 2, 3]
    row_length = len(row_input)
    row_output = customSum(row_input)
    data["params"][f"row-{i}-input"] = json.dumps(row_input)
    data["params"][f"row-{i}-length"] = row_length
    data["params"][f"row-{i}-output"] = row_output

    data["correct_answers"][f"row-{i}-output"] = row_output


def grade(data):

    i = 0
    if data["params"][f"row-{i}-fill-input"]:
        student_input = data["submitted_answers"][f"row-{i}-input"]
        student_length = data["submitted_answers"][f"row-{i}-length"]

        # If don't want students to be punished for using incorrect list syntax, do this in parse()
        # I don't know if parse() would overwrite the parse() for the other two inputs
        try:
            student_input = list(json.loads(student_input))
            student_sum = customSum(student_input)
        except Exception:
            data["format_errors"][f"row-{i}-input"] = (
                "You must input a valid list of numbers"
            )
            assignScore(data, i, 0)
            return  # or continue

        desired_output = data["params"][f"row-{i}-output"]
        if student_length == len(student_input) and student_sum == desired_output:
            assignScore(data, i, 1)
        else:
            assignScore(data, i, 0)
