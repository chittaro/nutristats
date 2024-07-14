import pandas as pd
import time
from helpers import *

'''
Returns dict with items filtered out
'''
def filterOut(halls = [], times = []) -> pd.DataFrame:
    halls = [hall.lower().replace(" ", "-") for hall in halls]
    
    df = pd.read_csv("../data/data.csv")

    # apply filters
    if len(halls) > 0:
        df = df[df["Dining_Hall"].isin(halls)]
    
    if len(times) > 0:
        df = df[df["Course"].isin(times)]

    return df

''' 
Returns dict of menu items based on filters & sort category (basic filter page)
'''
def getBestItems(halls: list, times: list, sort: str, ascend: bool) -> dict:
    sort = sort.replace(" ", "_")

    df = filterOut(halls, times)

    # apply sort
    df =  df.sort_values(by = [sort], ascending = ascend) 

    return df.to_dict(orient = "records")[:5]


'''
Returns dict of menu items for each meal category based on nutrition ranges (advanced filter page)
'''
def getMealPlan(halls: list, ranges: dict) -> list: # TODO: change to have real values

    df = filterOut(halls)

    breakfast_df = df[df["Course"] == "Breakfast"]
    breakfast_df = breakfast_df[list(ranges.keys())]
    lunch_df = df[df["Course"] == "Lunch"]
    lunch_df = lunch_df[list(ranges.keys())]
    dinner_df = df[df["Course"] == "Dinner"]
    dinner_df = dinner_df[list(ranges.keys())]

    # initialize series holding sums
    temp_sums = pd.Series(dict.fromkeys(ranges.keys(), 0))

    # initialize list of meals fitting requirements
    opt_meals = []

    # -- backtracking alg -- #

    # breakfast loop
    for b_index, b_row in breakfast_df.iterrows():
        
        if promising(b_row, temp_sums, ranges) == False:
            continue

        # lunch loop
        for l_index, l_row in lunch_df.iterrows():
            if promising(l_row, temp_sums, ranges) == False:
                continue

            # dinner loop
            for d_index, d_row in dinner_df.iterrows():
                if promising(d_row, temp_sums, ranges, True):
                    opt_meals.append([b_index, l_index, d_index])
                
                # end dinner
                temp_sums.subtract(d_row, fill_value = 0)

            # end lunch
            temp_sums.subtract(l_row, fill_value = 0)

        # end breakfast
        temp_sums.subtract(b_row, fill_value = 0)

    
    
    return opt_meals


start = time.time()
testRanges = {'Calories': [1500, 2500], 'Protein': [15, 30], 'Sugars': [0, 15], 'Dietary_Fiber': [10, 12]}
print(getMealPlan(['Bursley'], testRanges))

print(time.time() - start)