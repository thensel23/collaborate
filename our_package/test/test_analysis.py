#!/usr/bin/env python3

"""Unittests for the analysis module"""


import pytest
import numpy as np

import analysis as an


@pytest.fixture
def get_sample_data():
    data = np.array(
        [[0.0, 1.0, 2.0], [0.0, 0.0, 0.0], [2.0, 5.0, 3.0], [3.0, 3.0001, 2.9994]]
    )
    thresh = 0.01
    return data, thresh


@pytest.fixture
def get_sample_data_stripped():
    data_stripped = np.array(
        [
            [0.0, 1.0, 2.0],
            [2.0, 5.0, 3.0],
        ]
    )
    idx = np.array([0, 2])
    return data_stripped, idx


def test_check_if_significant(get_sample_data, get_sample_data_stripped):
    data_out, idx_out = an.check_if_significant_np(
        get_sample_data[0], get_sample_data[1]
    )
    np.testing.assert_array_equal(data_out, get_sample_data_stripped[0])
    np.testing.assert_array_equal(idx_out[0], get_sample_data_stripped[1])


@pytest.fixture
def get_ft_input():
    xs = np.linspace(0, 20, 100)
    ys = np.sin(xs * np.pi)
    tmax = len(xs)
    return ys, tmax


@pytest.fixture
def get_ft_result(get_ft_input):
    ft = np.fft.rfft(get_ft_input[0])
    freq = np.fft.rfftfreq(get_ft_input[1])
    return ft, freq


def test_do_DFT(get_ft_input, get_ft_result):
    ft, freq = an.do_DFT(*get_ft_input)
    np.testing.assert_array_equal(ft, get_ft_result[0])
    np.testing.assert_array_equal(freq, get_ft_result[1])
