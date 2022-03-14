# https://docs.gspread.org/en/latest/oauth2.html#oauth-client-id

import gspread

gc = gspread.oauth()

sh = gc.open("HouseAdvant16")

sh.sheet1.get('A1:B3')

import pandas as pd
from gspread_pandas import Spread, Client

file_name = "http://stats.idre.ucla.edu/stat/data/binary.csv"
df = pd.read_csv(file_name)

spread = Spread('Example Spreadsheet')

spread.df_to_sheet(df, index=False, sheet='New Test Sheet', start='A2', replace=True)
