import matplotlib.pyplot as plt
from matplotlib import colors
import io
import random
import numpy as np
import prairielearn as pl

def generate(data):
    data['params']['num1'] = 3
    data['params']['num2'] = random.randint(1, 5)
    return data


def file(data):

    if data['filename']=='fig1.png':
        fig = plt.figure(figsize=(4, 4), dpi=100)
        fig.text(
            0.5, 0.5,
            data['params']['num1'],
            ha="center",
            va="center",
            fontsize=80
        )
    if data['filename']=='fig2.png':
            fig = plt.figure(figsize=(4, 4), dpi=100)
            fig.text(
                0.5, 0.5,
                data['params']['num2'],
                ha="center",
                va="center",
                fontsize=80
            )

    # Save the figure and return it as a buffer
    buf = io.BytesIO()
    plt.savefig(buf,format='png')
    return buf
