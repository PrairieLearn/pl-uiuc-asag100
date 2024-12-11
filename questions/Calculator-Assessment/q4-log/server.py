import random
import math

def generate(data):
    # Simulate values
    a = round(random.random() + 1, 2)

    x = math.log(a*(10**-4), 10)  
    y = math.log(a*(10**-4)) 
    z = math.log(a*(10**-4), 2)  
    # Release parameters
    data["params"]["a"] = a
    data["correct_answers"]["x"] = x
    data["correct_answers"]["y"] = y
    data["correct_answers"]["z"] = z