#!/usr/bin/env python3

"""Unit tests for the analysis module."""

import sys
import unittest
import numpy as np

sys.path.append("../our_package")
from analysis import check_if_significant_np  # noqa


class TestSignificant(unittest.TestCase):
    def test_significant(self):
        """
        Test if the the function return what it should do:
        """
        print("bla")
        data = np.array(
            [[0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 2.0, 0.0], [2.0, 0.0, 3.0, 1.2]]
        ).T

        threshold = 0.01

        actual_result_array = np.array(
            [[0.0, 1.0, 0.0], [1.0, 2.0, 0.0], [2.0, 3.0, 1.2]]
        ).T

        actual_result_idx = np.array([0, 2, 3])

        result_nparray, result_idx = check_if_significant_np(data, threshold)
        # self.assertEqual(result_nparray, actual_result_array)
        # self.assertEqual(result_idx, actual_result_idx)
        self.assertTrue((result_nparray == actual_result_array).all())
        self.assertTrue((result_idx[0] == actual_result_idx).all())
