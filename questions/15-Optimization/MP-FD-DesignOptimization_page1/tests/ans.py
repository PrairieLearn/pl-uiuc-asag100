import numpy as np

xvec1 = np.array(data['params']['xvec1']['_value'])

xvec2 = np.array(data['params']['xvec2']['_value'])

def get_change(xvec1, xvec2):
    change = np.max(np.abs(xvec1-xvec2))
    return change
