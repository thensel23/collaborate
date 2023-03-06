"""
Analysis module.

@Team 1, 03/23
"""

import numpy as np
import matplotlib.pyplot as plt


def check_if_significant(data, thresh):
    """Check variance of columns and select the ones above a threshold.

    :param data: dataframe to inspect
    :param thresh: threshold for variance
    """
    data_out = data.drop(data.var()[data.var() < thresh].index.values, axis=1)
    indices = data.var()[data.var() > thresh].index.values
    return data_out, indices


def check_if_significant_np(data, thresh):
    indices = np.nonzero(np.var(data, axis=1) > thresh)
    data_out = data[indices]
    return data_out, indices


def get_correlation_measure(df):
    """Get correlations within columns of a dataframe.

    :param df: dataframe
    :type df: pandas dataframe
    """
    drop_values = set()  # an unordered collection of items
    cols = df.columns  # get the column labels
    print(cols)
    for i in range(0, df.shape[1]):
        for j in range(
            0, i + 1
        ):  # get rid of all diagonal entries and the lower triangular
            drop_values.add((cols[i], cols[j]))
    print(drop_values)
    return drop_values


def euclidean_distance(list_ref, list_comp, vectors):
    distances = np.zeros(len(list_ref))
    for i in range(len(list_ref)):
        distances[i] = np.linalg.norm(vectors[list_comp[i]] - vectors[list_ref[i]])
    return distances


def do_DFT(data, tmax):
    data_s = np.fft.rfft(data)
    data_w = np.fft.rfftfreq(tmax)
    return data_s, data_w


def plot_ft(freq, spec):
    """plot the Fouriertrans of the data"""
    fig, ax = plt.subplots()
    power_spec = np.abs(spec) ** 2
    ax.plot(freq, power_spec)
    ax.set_xlabel("frequency")
    ax.set_ylabel("power")
    plt.show()


def do_fft(data, tmax):
    data_s = np.fft.fft(data)
    data_w = np.fft.fftfreq(tmax)
    # only take the positive frequency components
    return data_w[0 : tmax // 2], data_s[0 : tmax // 2]


def calc_auto(wavef):
    aucofu = np.zeros(len(wavef[0]), dtype=complex)
    for i in range(0, len(wavef[0])):
        aucofu[i] = np.sum(wavef[:, 0] * np.conjugate(wavef[:, i]))
    return aucofu
