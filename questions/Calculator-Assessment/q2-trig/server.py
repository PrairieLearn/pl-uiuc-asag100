import random
import math


def generate(data):
    ang = random.randint(40, 50)
    trig_value = round(random.random(), 2)
    rad = math.sin(ang) * math.acos(trig_value)
    deg = math.sin(ang * math.pi / 180) * (math.acos(trig_value) * 180 / math.pi)
    
    data["params"]["ang"] = ang
    data["params"]["trig_value"] = trig_value
    data["correct_answers"]["deg"] = deg
    data["correct_answers"]["rad"] = rad
