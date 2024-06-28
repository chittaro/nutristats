from scrape_funcs import *
from utils import *
import pandas as pd
import os
from grader import *
import sqlalchemy as sql
from datetime import date



# -- parse data -- #
menu_dict = getStartDict()

hallDirs = os.listdir('../data/hall_HTML')
for dir in hallDirs:
    getDhallItems('../data/hall_HTML/', dir, menu_dict)

# -- convert to pandas df -- #
df = pd.DataFrame(menu_dict)
df = scoreMenu(df)

# -- convert to csv -- #
df.to_csv("data.csv")

# -- create file -- #
path = 'home/chittaro/python/nutristats/source/data/'
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print(d1)


#with open('/home/chittaro/python/nutristats/source/data/input2.txt', 'a') as file:
#    file.write('wroted it\n')
