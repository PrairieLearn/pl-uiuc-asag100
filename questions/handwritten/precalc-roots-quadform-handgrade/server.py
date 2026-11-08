import prairielearn as pl
import sympy as sp
import random

def generate(data):
    x = sp.symbols("x")
    C = random.randint(1, 3)
    f = 5*x**3 - x**2 - C*x
    D = 1+C*20
    
    data['params']['D'] = D 
    data["params"]["f"] = sp.latex(f)