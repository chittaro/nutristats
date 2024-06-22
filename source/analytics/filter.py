import pandas as pd

def getBestItems(halls: list, times: list, sort: str) -> dict:
    df = pd.read_csv("data/data.csv")

    if len(halls) > 0:
        df = df[df["Dining_Hall"].isin(halls)]
    
    if len(times) > 0:
        df = df[df["Course"].isin(times)]

    df =  df.sort_values(by = [sort], ascending = False) 


    return df.to_dict(orient = "records")
