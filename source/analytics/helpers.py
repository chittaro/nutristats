import pandas as pd


'''
Check if meal choices meet nutrition ranges
'''
# TODO: (in future) change so "good enough" score is calculated initially, similar to FASTTSP called in OPTTSP
def promising(menu_row: pd.Series, sums: pd.Series, ranges: dict, lower_bound = False) -> bool:

    sums.add(menu_row)

    for column in ranges:
        if inRange(menu_row[column], ranges[column], lower_bound) == False:
            sums.subtract(menu_row)
            return False

    return True

'''
Check if value is within a range
'''
def inRange(val: int, range: list, lower_bound: bool) -> bool:
    if val <= range[1]:
        if lower_bound == False:
            return True
        else:
            return val >= lower_bound
    
    return False