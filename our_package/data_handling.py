"""Data import routines"""

import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_in_df(filedir, filename):
    """Load data from testfile using pandas"""
    name = "{}{}".format(filedir, filename)
    print("Reading from file {} - pandas".format(name))
    data = pd.read_csv(name, r"\s+")
    return data


def read_in_np(filedir, filename):
    """Load data from testfile using numpy"""
    name = os.path.join(filedir, filename)
    print("Reading from file {} - numpy".format(name))
    data = np.loadtxt(name, skiprows=1)
    data = data.T
    return data


def plot_columns(data):
    """Plot the data for visiual inspection."""
    fig, ax = plt.subplots(len(data) - 1, 1, sharex=True)
    for i in range(1, len(data)):
        ax[i - 1].plot(data[0], data[i])
        ax[i - 1].set_title("Column {}".format(i))
    fig.suptitle("first visual inspection")
    plt.show()
