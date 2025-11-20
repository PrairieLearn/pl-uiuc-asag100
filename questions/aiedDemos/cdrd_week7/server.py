import random, copy, json
import os.path
from pythonHelper import *
from nlpHelper import *

qs = [
  { "tag": "a3_is_list_sorted",
    "notes": "Assume that the variable <code>x</code> is a list of numbers.",
    "code": "def f(x):\n    for i in range(1, len(x)):\n        if x[i-1] > x[i]:\n            return False\n    return True",
    "range": "2-5",
    "first":  "Return True if the list is sorted from smallest to biggest.  Otherwise, return False.",
    "second": "return True if the numbers in a list are non-decreasing; otherwise return False",
    "third":  "Return a Boolean indicating whether the list is sorted from smallest to largest or not",
    "model": "0"},

  # { "tag": "a33_replace_all_ys_with_zs",
  #   "notes": "Assume that the variable <code>x</code> is a list of integers and variables <code>y</code> and <code>z</code> are integers.",
  #   "code": "def f(x, y, z):\n    for idx,val in enumerate(x):\n        if val == y:\n            x[idx] = z",
  #   "range": "2-4",
  #   "first":  "Replace every element equal to y in the given list with the value z",
  #   "second": "Find and replace all values in the given list equal to y with z",
  #   "third":  "Modify the list x so that all values y are set to the value z",
  #   "model": "1"},

  # { "tag": "a13y_reverse_a_list_in_place",
  #   "notes": "Assume that the variable <code>x</code> is a list.",
  #   "code": "def f(x):\n    x.reverse()",
  #   "range": "2-2",
  #   "first":  "Reverse the given list in place",
  #   "second": "Reverse the order of the list's elements.  Returns None",
  #   "third":  "Modify the provided list so that its elements are reversed",
  #   "model": "2"},

  # { "tag": "a13x_create_a_reversed_version_of_a_list",
  #   "notes": "Assume that the variable <code>x</code> is a list.",
  #   "code": "def f(x):\n    return list(reversed(x))",
  #   "range": "2-2",
  #   "first":  "Return a copy of given list with the elements reversed",
  #   "second": "Make a reversed version of a list and return it",
  #   "third":  "return a new list containing the provided lists elements in the reverse order",
  #   "model": "3"},

  # { "tag": "a18_sum_of_even_indexed_elements",
  #   "notes": "Assume that the variable <code>x</code> is a list of numbers.",
  #   "code": "def f(x):\n    y = 0\n    for i in range(0, len(x), 2):\n        y += x[i]\n    return y",
  #   "range": "2-5",
  #   "first":  "Return the sum of the elements in the given list with even indices",
  #   "second": "Return the total computed by adding together every other element, starting with the zeroth element",
  #   "third":  "add together a list's even-indexed elements and return the result",
  #   "model": "4"},

  # { "tag": "a19_count_number_of_even_numbers_in_a_list",
  #   "notes": "Assume that the variable <code>x</code> is a list of integers.",
  #   "code": "def f(x):\n    y = 0\n    for val in x:\n        if val % 2 == 0:\n            y += 1\n    return y",
  #   "range": "2-6",
  #   "first":  "Return a count of the number of list elements that are even.",
  #   "second": "Return the number of even-valued elements in the given list",
  #   "third":  "count how many elements in the given list are even and return the count",
  #   "model": "5"},

  # { "tag": "a24_print_even_values_in_list",
  #   "notes": "Assume that the variable <code>x</code> is a list of integers.",
  #   "code": "def f(x):\n    for val in x:\n        if val % 2 == 0:\n            print(val)",
  #   "range": "2-4",
  #   "first":  "Print all of the even values in the given list",
  #   "second": "Print each value from the list x where the value is evenly divisible by two",
  #   "third":  "print the even list values.  The function returns None.",
  #   "model": "6"},

  # { "tag": "a25_do_lists_have_same_contents",
  #   "notes": "Assume that the variables <code>x</code> and <code>y</code> are both lists.",
  #   "code": "def f(x, y):\n    return x == y",
  #   "range": "2-2",
  #   "first":  "Return True if two lists have the same contents; otherwise return False",
  #   "second": "Return a Boolean indicating whether two lists have the same contents or not",
  #   "third":  "compare two lists, if they have the same contents return True, else return False.",
  #   "model": "7"},

  # { "tag": "a32_are_there_duplicates_in_a_list",
  #   "notes": "Assume that the variable <code>x</code> is a list.",
  #   "code": "def f(x):\n    for val in x:\n        if x.count(val) > 1:\n            return True\n    return False",
  #   "range": "2-5",
  #   "first":  "Return True if there are any duplicates in the given list.  Otherwise, return False.",
  #   "second": "Return False if every element in the provided list is unique.  Otherwise, return True.",
  #   "third":  "returns a Boolean indicating whether there are duplicates in a list",
  #   "model": "8"},

  # { "tag": "a36_copy_a_list",
  #   "notes": "Assume that the variable <code>x</code> is a list.",
  #   "code": "def f(x):\n    return x[:]",
  #   "range": "2-2",
  #   "first":  "Return a copy of the given list",
  #   "second": "Make a copy of the provided list and return it",
  #   "third":  "Copies the list passed as a parameter",
  #   "model": "9"},

  # { "tag": "a45_are_lists_same_length",
  #   "notes": "Assume that the variables <code>x</code> and <code>y</code> are both lists.",
  #   "code": "def f(x, y):\n    return len(x) == len(y)",
  #   "range": "2-2",
  #   "first":  "Returns True if the two given lists have the same length; otherwise return False",
  #   "second": "Checks if two lists are the same length",
  #   "third":  "Returns true if both parameters have the same number of elements",
  #   "model": "10"},

  # { "tag": "a46_print_non-empty_strings",
  #   "notes": "Assume that the variable <code>x</code> is a list of strings.",
  #   "code": "def f(x):\n    for val in x:\n        if len(val) > 0:\n            print(val)",
  #   "range": "2-4",
  #   "first":  "Print all of the non-empty strings in the given list",
  #   "second": "Print every string from the list x that isn't the empty string",
  #   "third":  "Output all of the strings that have at least one character",
  #   "model": "11"},

  # { "tag": "a47_extracts_strings_from_a_mixed_type_list",
  #   "notes": "Assume that the variable <code>x</code> is a list containing a variety of types.",
  #   "code": "def f(x):\n    y = []\n    for val in x:\n        if type(val) == str:\n            y.append(val)\n    return y",
  #   "range": "2-6",
  #   "first":  "Return a copy of a given list containing only the strings",
  #   "second": "Filter a given list to produce a list containing only the elements that are strings.",
  #   "third":  "Return a new list that has only the strings from the provided list",
  #   "model": "12"},

  # { "tag": "a48_produce_a_list_without_duplicates",
  #   "notes": "Assume that the variable <code>x</code> is a list.",
  #   "code": "def f(x):\n    y = []\n    for val in x:\n        if val not in y:\n            y.append(val)\n    return y",
  #   "range": "2-6",
  #   "first":  "Return a copy of the given list without duplicates",
  #   "second": "Make a copy of x, but make sure there is only one copy of each value.",
  #   "third":  "Return a new list with a single copy of each value in the provided list",
  #   "model": "13"},

#  { "tag": "",
#    "notes": "Assume that the variables <code>x</code> and <code>y</code> are strings.",
#    "code": "",
#    "range": "-",
#    "first": "",
#    "second": "",
#    "third": "",
#    "model": ""},


]


def generate(data):

    q = random.choice(qs)

    data['params']['notes'] = q['notes']
    data['params']['code'] = q['code']
    data['params']['range'] =  q['range']
    data['correct_answers']['tag'] = q['tag']
    data['correct_answers']['model'] = q['model']
    data['correct_answers']['first'] = q['first']
    data['correct_answers']['second'] = q['second']
    data['correct_answers']['third'] = q['third']
    data['params']['model_file_name'] = q['model'] + '.pkl'


def grade(data):
    server_files_course_path = data["options"]["client_files_course_path"].replace('clientFilesCourse', 'serverFilesCourse')
    nltk_data_path = os.path.join(server_files_course_path, 'nltk_data')
    vocab_path = os.path.join(server_files_course_path, 'vocabulary.pkl')

    model_path = data['params']['model_file_name']
    response = data["submitted_answers"]["result"]
    nlp_score = nlp_grade_response(nltk_data_path, model_path, response)
    tokens_list = tokenize(unescape_response(response), nltk_data_path)
    data["feedback"]["is_garbage"] = not nlp_score and nlp_detect_garbage(tokens_list, vocab_path)
    # TODO, decide what to do, the line below is definitely not desirable
    data["score"] = nlp_score