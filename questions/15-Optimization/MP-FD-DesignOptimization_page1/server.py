import matplotlib.pyplot as plt
from matplotlib import colors
import io
import random
import numpy as np
import prairielearn as pl

def generate(data):
    names_for_user = [

    ]
    names_from_user = [
        {"name": "xvec1", "description": "design variables corresponding to first figure",
         "type": "1d numpy array"},
        {"name": "xvec2", "description": "design variables corresponding to second figure",
         "type": "1d numpy array"},
        {"name": "get_change",
         "description": "returns maximum absolute difference between two arrays",
         "type": "function"},
    ]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user

    nelx = 3
    nely = 2
    data["params"]["nelx"] = nelx
    data["params"]["nely"] = nely

    xvec1 = [np.random.choice([0.0,0.2,0.3,0.5,0.7,1.0]) for i in range(nelx*nely)]
    xvec1 = np.round(xvec1,2)
    data["params"]["xvec1"] = pl.to_json(xvec1)

    xvec2 = [np.random.choice([0.0,0.2,0.3,0.5,0.7,1.0]) for i in range(nelx*nely)]
    xvec2 = np.round(xvec2,2)
    data["params"]["xvec2"] = pl.to_json(xvec2)
    return data


def file(data):

    if data['filename']=='fig1.png':
        # create plt
        xvec = pl.from_json(data['params']['xvec1'])
        X = xvec.reshape((data["params"]["nelx"],data["params"]["nely"]))
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        plt.imshow(-X.T, cmap='gray',interpolation='none', norm=colors.Normalize(vmin=-1,vmax=0) )
        for i in range(data["params"]["nelx"]):
            for j in range(data["params"]["nely"]):
                if X[i, j] < .7:
                    plt.text(i-.1,j+.1,X[i,j], color='black', fontsize=30, weight='bold')
                else:
                    plt.text(i-.1,j+.1,X[i,j], color='white', fontsize=30, weight='bold')

        plt.xticks([])
        plt.yticks([])

    if data['filename']=='fig2.png':
        # create plt
        xvec = pl.from_json(data['params']['xvec2'])
        X = xvec.reshape((data["params"]["nelx"],data["params"]["nely"]))
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        plt.imshow(-X.T, cmap='gray',interpolation='none', norm=colors.Normalize(vmin=-1,vmax=0)  )
        for i in range(data["params"]["nelx"]):
            for j in range(data["params"]["nely"]):
                if X[i, j] < .7:
                    plt.text(i-.1,j+.1,X[i,j], color='black', fontsize=30, weight='bold')
                else:
                    plt.text(i-.1,j+.1,X[i,j], color='white', fontsize=30, weight='bold')
        plt.xticks([])
        plt.yticks([])

    # Save the figure and return it as a buffer
    buf = io.BytesIO()
    plt.savefig(buf,format='png')
    return buf
