import pandas as pd
from IPython.core.display import display

football = pd.read_csv('data_sf.csv')
display(football.info())