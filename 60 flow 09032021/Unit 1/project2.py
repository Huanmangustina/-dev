from typing import Any, Union

import pandas as pd
from IPython.core.display import display
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

football: Union[Union[TextFileReader, Series, DataFrame, None], Any] = pd.read_csv("data_sf.csv")
football[football.Age.max()].Reactions.mean()
