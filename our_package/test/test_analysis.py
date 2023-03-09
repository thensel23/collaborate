import analysis
import pytest
import pandas as pd


@pytest.fixture
def get_sample_data():
    data = {"col1": [1, 2], "col2": [0, 0]}
    df = pd.DataFrame(data=data)
    thresh = 0.1
    return df, thresh


def test_check_if_significant(get_sample_data):
    data_out, indices = analysis.check_if_significant(
        get_sample_data[0], get_sample_data[1]
    )
    ref_data = {"col1": [1, 2]}
    ref_df = pd.DataFrame(data=ref_data)
    pd.testing.assert_frame_equal(data_out, ref_df)
    assert indices == ["col1"]
