import pandas as pd


# Define cals/gram per macros
CALS_FAT = 9
CALS_CRB = 4
CALS_PRO = 4

def scoreMenu(df: pd.DataFrame) -> pd.DataFrame:
    '''Adds a column of total scores to the dataframe'''

    # Declare empty list and dict
    totals = []
    scores = []

    # Iterate through rows and calculate scores
    for index, row in df.iterrows():
        scrs = calcScores(row)
        totals.append(scrs["Total"])
        scrs["Menu_Item"] = row["Menu_Item"]
        scores.append(scrs)

    # Assign totals to a new column in the df
    df["Nutrition_Score"] = totals
    
    print(df)

    # Return dict
    return df
    
def calcScores(row: pd.Series) -> dict:
    '''Calculates each category score (and total) for item. Returns dictionary with categories as keys and scores as vals.'''

    # Calculate subscores
    sc_tf = 1 if row["Trans_Fat"] == 0 else 0
    sc_sf = round(1 - (CALS_FAT * row["Saturated_Fat"] / row["Calories"]), 2)
    sc_sd = round(1 - (row["Sodium"] / row["Calories"]), 2)
    sc_pr = round(CALS_PRO * row["Protein"] / row["Calories"], 2)
    sc_cb = round(1 if row["Total_Carbohydrate"] == 0 else row["Dietary_Fiber"] / row["Total_Carbohydrate"], 2)

    # Sum
    total = round(sc_tf + sc_sf + sc_sd + sc_pr + sc_cb, 2)

    # Return dict
    scores = {"Calories": row["Calories"],
              "Trans Fat": sc_tf,
              "Sat. Fat": sc_sf,
              "Sodium": sc_sd,
              "Protein": sc_pr,
              "Fiber": sc_cb,
              "Total": total}
    
    return scores
