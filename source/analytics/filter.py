import pandas as pd

def getBestItems(halls: list, times: list, sort: str, ascend: bool) -> dict:
    df = pd.read_csv("data/data.csv")

    if len(halls) > 0:
        df = df[df["Dining_Hall"].isin(halls)]
    
    if len(times) > 0:
        df = df[df["Course"].isin(times)]

    df =  df.sort_values(by = [sort], ascending = ascend) 


    return df.to_dict(orient = "records")[:5]
