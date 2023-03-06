from settings import *
from analysis import *
from data_handling import *

import pathlib

path = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":

    try:
        fname = FILENAMES[0]
        dir = FILEDIR
        df = read_in_df(dir, fname)

        # add some code here

        # add some code here

        print(df.head())
        # plot_columns(df)
    except:
        raise Exception("something went terribly wrong!")
