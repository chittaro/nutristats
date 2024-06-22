from scrape_funcs import *
from utils import *
import pandas as pd
import os
from grader import *

menu_dict = getStartDict()

hallDirs = os.listdir('../data/hall_HTML')
for dir in hallDirs:
    getDhallItems('../data/hall_HTML/', dir, menu_dict)

df = pd.DataFrame(menu_dict)
df = scoreMenu(df)

df.to_csv("data.csv")