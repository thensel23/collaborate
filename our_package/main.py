"""This is the main routine of our package!

Here, all the subroutines are executed and the results are stored whereever...
"""

from settings import THRESHV
from analysis import check_if_significant_np, do_DFT, plot_ft
from data_handling import read_in_np, plot_columns


def numerical():

    # data file:
    datafolder = "../data"
    datafile = "efield.t"
    data = read_in_np(datafolder, datafile)
    plot_columns(data)
    cleared_data, _ = check_if_significant_np(data, THRESHV)
    spec, freq = do_DFT(cleared_data, len(cleared_data[0]))
    print(spec.shape)
    print(freq)
    plot_ft(freq, spec[1])


if __name__ == "__main__":
    numerical()
