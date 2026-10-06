import random

def generate(data):

    description = "Sorts the argument input list (nums) in descending order"

    names_for_user = [ ]
    names_from_user = [
    {'name': 'list_sort', 'description': description, 'type': "function"}]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user

    return data
