import random
import numpy as np
import math


def generate(data):

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    l1 = random.randint(1, 10)
    l2 = random.randint(1, 10)
    
    den = b*c - a*d

    if (den == 0):
        return generate(data)
    
    xnum = b * l2 - d * l1
    ynum = l1 * c - a * l2

    data["params"]["arep"] = f"\\begin{{pmatrix}}{a} & {b}\\\\ {c} & {d}\\end{{pmatrix}}"
    data["params"]["brep"] = f"\\begin{{pmatrix}}{l1}\\\\{l2}\\end{{pmatrix}}"



    data["params"]["xrep"] = f"\\begin{{pmatrix}}\\frac{{{xnum // math.gcd(xnum, den)}}}{{{den // math.gcd(xnum, den)}}}\\\\ \\frac{{{ynum // math.gcd(ynum, den)}}}{{{den // math.gcd(ynum, den)}}}\\end{{pmatrix}}"

    estx = round(xnum/den)
    esty = round(ynum/den)

    data["params"]["estrep"] = f"\\begin{{pmatrix}}{estx}\\\\{esty}\\end{{pmatrix}}"
    data["params"]["errrep"] = f"\\begin{{pmatrix}}\\frac{{{-(estx * den - xnum) // math.gcd((estx * den - xnum), den)}}}{{{den // math.gcd((estx * den - xnum), den)}}}\\\\ \\frac{{{-(esty * den - ynum) // math.gcd((esty * den - ynum), den)}}}{{{den // math.gcd((esty * den - ynum), den)}}}\\end{{pmatrix}}"
    data["params"]["resrep"] = f"\\begin{{pmatrix}}{-(a * estx + b * esty - l1)}\\\\{-(c * estx + d * esty - l2)}\\end{{pmatrix}}"
    data["params"]["negerrrep"] = f"\\begin{{pmatrix}}\\frac{{{(estx * den - xnum) // math.gcd((estx * den - xnum), den)}}}{{{den // math.gcd((estx * den - xnum), den)}}}\\\\ \\frac{{{(esty * den - ynum) // math.gcd((esty * den - ynum), den)}}}{{{den // math.gcd((esty * den - ynum), den)}}}\\end{{pmatrix}}"
    data["params"]["negresrep"] = f"\\begin{{pmatrix}}{a * estx + b * esty - l1}\\\\{c * estx + d * esty - l2}\\end{{pmatrix}}"

    if (np.linalg.norm(np.array([(estx * den - xnum)/den, (esty * den - ynum)/den])) >= np.linalg.norm([a * estx + b * esty - l1, c * estx + d * esty - l2])):
        return generate(data)

