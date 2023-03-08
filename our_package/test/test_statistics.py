import statistics
import pytest
import settings
import pandas as pd


# using the tmp_path pytest fixture for temporary paths
def test_plot_relevant(tmp_path):
    df = pd.read_csv("./test/data/test_data.csv", sep=r"\s+")
    # write file to temporary directory
    outname = "/test"
    statistics.plot_relevant(df, settings.THRESHV, tmp_path.resolve(), outname)
    assert len(list(tmp_path.iterdir())) == 1