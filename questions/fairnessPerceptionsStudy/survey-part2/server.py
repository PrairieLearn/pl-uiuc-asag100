def grade(data):
    data["score"] = 1

    for num in range(7):
        data["partial_scores"][f"q{num}"] = {"score": None}
