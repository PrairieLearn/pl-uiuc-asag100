import os
import random


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
