"""This is the main routine of our package!

Here, all the subroutines are executed and the results are stored whereever...
"""

import matplotlib.pyplot as plt
from settings import *  # noqa
from analysis import *  # noqa
from data_handling import read_in_np, plot_columns


def numerical(plot=False):
    # data file:
    datafolder = "../data"
    datafile = "efield.t"
    data = read_in_np(datafolder, datafile)

    efield2, _ = check_if_significant_np(data, 0.00001)
    efourier, freqs = do_DFT(data, len(efield2[0]))

    if plot:
        plot_columns(data, "electric field: raw data")
        plot_columns(efield2, "electric field: filtered")
        plt.plot(
            freqs, abs(efourier) ** 2
        )  # the frequency of this laser pulse was 0.116
        plt.show()


if __name__ == "__main__":
    numerical(plot=True)
