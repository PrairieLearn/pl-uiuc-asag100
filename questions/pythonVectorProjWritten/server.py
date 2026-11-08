import random
import numpy as np
from pl_random import *
from pl_template import *
from pl_geom import *
from pl_draw import *
import prairielearn as pl
def generate(data):
	a = randIntNonZeroArray(3, -9, 9)
	b = randIntNonZeroArray(3, -9, 9)
	c = np.dot(a,b)/np.dot(b,b) * b

	data['params']['a_vec'] = cartesianVector(a)
	data['params']['b_vec'] = cartesianVector(b)
	data['params']['a'] = pl.to_json(a)
	data['params']['b'] = pl.to_json(b)
	data['correct_answers']['cx'] = c[0]
	data['correct_answers']['cy'] = c[1]
	data['correct_answers']['cz'] = c[2]

	data['correct_answers']['a_dot_b'] = int(np.dot(a,b))
	data['correct_answers']['b_dot_b'] = int(np.dot(b,b))
	data['correct_answers']['c_vec'] = cartesianVector(c)

	return data