from settings import *
from analysis import *
from data_handling import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_relevant(df, threshv, output_path: str, output_name: str):
    """Plots significant data in pairplot and save plot as PDF

    Args:
        df: Pandas DataFrame object with numerical values
        threshv: the threshhold value that filters out insignificant data
        output_path: to which directory will the PDF be saved
        output_name: the name of the PDF

    Returns:
        A dataframe with significant data
    """
    df, indices = check_if_significant(df, threshv)
    print(indices)
    sns.pairplot(df, corner=True)
    save_path = f"{output_path}{output_name}.pdf"
    plt.savefig(save_path)


def plot_correlation(df, threshv, output_path, output_name):
    """Plots correlation of significant data in heatmap and save plot as PDF

    Args:
        df: Pandas DataFrame object with numerical values
        threshv: the threshhold value that filters out insignificant data
        output_path: to which directory will the PDF be saved
        output_name: the name of the PDF

    Returns:
        A dataframe with significant data
    """
    df, indices = check_if_significant(df, threshv)
    print(indices)
    df_short = df.drop(["time"], axis=1)
    df_corr = df_short.corr()
    matrix = np.triu(df_corr)
    plot = sns.heatmap(df_corr, annot=True, mask=matrix)
    save_path = f"{output_path}{output_name}.pdf"
    fig = plot.get_figure()
    fig.savefig(save_path)


### Testing
if __name__ == "__main__":
    # relevant data
    df = read_in_df(FILEDIR, FILENAMES[2])
    plot_relevant(df=df, threshv=THRESHV, output_path=OUTDIR, output_name="test1")

    # correlation
    df = read_in_df(FILEDIR, FILENAMES[0])
    plot_correlation(df=df, threshv=THRESHV, output_path=OUTDIR, output_name="test1")
