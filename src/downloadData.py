# author: Sicheng Marc Sun
# date: 2020-11-19

"""This script downloads data from a given URL

Usage: downloadData.py --file_path=<file_path>  --saving_path=<saving_path>

Options:
--file_path=<file_path>   Path to the data file
--saving_path=<saving_path> 
"""

import pandas as pd
from docopt import docopt

opt = docopt(__doc__)


def main(file_path, saving_path):
    # read in data
    df = pd.read_csv(file_path)

    df.to_csv(saving_path)


# standard error function


if __name__ == "__main__":
    main(opt["--file_path"], opt["--saving_path"])