import pandas as pd

''' 
Returns list of menu items based on filters & sort category 
'''
def getBestItems(halls: list, times: list, sort: str, ascend: bool) -> dict:
    halls = [hall.lower().replace(" ", "-") for hall in halls]
    sort = sort.replace(" ", "_")

    df = pd.read_csv("data/data.csv")

    # apply filters
    if len(halls) > 0:
        df = df[df["Dining_Hall"].isin(halls)]
    
    if len(times) > 0:
        df = df[df["Course"].isin(times)]

    # apply sort
    df =  df.sort_values(by = [sort], ascending = ascend) 

    return df.to_dict(orient = "records")[:5]
