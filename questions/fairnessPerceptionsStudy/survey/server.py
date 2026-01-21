def grade(data):
    data["score"] = 1

    for num in range(11):
        data["partial_scores"][f"q{num}"] = {"score": None}
