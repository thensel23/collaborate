"""This is the main routine of our package!

Here, all the subroutines are executed and the results are stored whereever...
"""

from settings import *  # noqa
from analysis import *  # noqa
from data_handling import read_in_np, plot_columns


def numerical():

    # data file:
    datafolder = "../data"
    datafile = "efield.t"
    data = read_in_np(datafolder, datafile)
    plot_columns(data)


if __name__ == "__main__":
    numerical()
