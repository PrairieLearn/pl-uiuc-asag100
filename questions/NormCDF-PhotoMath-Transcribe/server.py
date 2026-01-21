import random
import matplotlib.pyplot as plt
import numpy as np
import io
import scipy.stats as stats

def generate(data):
    mu = round(random.uniform(8, 14), 2)
    sigma = round(random.uniform(.4, .6), 2)

    minlen = round(random.uniform(mu - 2, mu - 1) * 2, 0) / 2
    maxlen = round(random.uniform(mu + 1, mu + 2) * 2, 0) / 2

    data["params"]["mu"] = mu
    data["params"]["sigma"] = sigma
    data["params"]["minlen"] = minlen
    data["params"]["maxlen"] = maxlen

def file(data):
    if data["filename"] == "figure.png":
        mu = data["params"]["mu"]
        sigma = data["params"]["sigma"]
        x = np.linspace(mu - 3, mu + 3, 1000)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))
        xt = np.linspace(round(2 * (mu - 3))/2, round(2 * (mu + 3))/2, 13)
        plt.xticks(xt)
        plt.grid()
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        return buf
