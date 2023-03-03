import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_in_df(filedir, filename):
    name = "{}{}".format(filedir, filename)
    print("Reading from file {} - pandas".format(name))
    data = pd.read_csv(name, r"\s+")
    return data


def read_in_np(filedir, filename):
    name = "{}{}".format(filedir, filename)
    print("Reading from file {} - numpy".format(name))
    data = np.loadtxt(name, skiprows=1)
    data = data.T
    return data


def plot_columns(data):
    for i in range(1, len(data)):
        plt.plot(data[0], data[i])
        plt.title("Column {}".format(i))
        plt.show()
