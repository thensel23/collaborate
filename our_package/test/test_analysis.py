#!/usr/bin/env python3

# bla bla

"""Unittests for the analysis module"""

import pytest
import analysis
import pandas as pd
import numpy as np


@pytest.fixture
def get_sample_data():
    data = np.array(
        [[0.0, 1.0, 2.0], [0.0, 0.0, 0.0], [2.0, 5.0, 3.0], [3.0, 3.0001, 2.9994]]
    )
    thresh = 0.01
    return data, thresh


@pytest.fixture
def get_sample_data_pd():
    data = {"col1": [1, 2], "col2": [0, 0]}
    df = pd.DataFrame(data=data)
    thresh = 0.1
    return df, thresh


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
    data_out, idx_out = analysis.check_if_significant_np(
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
    ft, freq = analysis.do_DFT(*get_ft_input)
    np.testing.assert_array_equal(ft, get_ft_result[0])
    np.testing.assert_array_equal(freq, get_ft_result[1])


@pytest.fixture
def get_wavedata():
    wave = np.array([[0.0, 0.1], [0.2, 0.4], [0.1, 0.2], [0.1, 0.1]])
    auto_corr = np.array([0.06 + 0.0j, 0.11 + 0.0j])
    return wave, auto_corr


def test_calc_auto(get_wavedata):
    res = analysis.calc_auto(get_wavedata[0])
    np.testing.assert_array_almost_equal(res, get_wavedata[1])
    data = {"col1": [1, 2], "col2": [0, 0]}
    df = pd.DataFrame(data=data)
    thresh = 0.1
    return df, thresh


def test_check_if_significant(get_sample_data_pd):
    data_out, indices = analysis.check_if_significant(
        get_sample_data_pd[0], get_sample_data_pd[1]
    )
    ref_data = {"col1": [1, 2]}
    ref_df = pd.DataFrame(data=ref_data)
    pd.testing.assert_frame_equal(data_out, ref_df)
    assert indices == ["col1"]
