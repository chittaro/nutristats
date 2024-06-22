from bs4 import BeautifulSoup


# TODO: find way to automate curling process (need to update textfile every day)
def getSoup(path: str, file: str) -> BeautifulSoup:

    data = open(path + file, "r")
    bs = BeautifulSoup(data, "html.parser")
    data.close()

    return bs

def getStartDict() -> dict:
    nutritionDict = {
    "Dining_Hall": [],
    "Course": [],
    "Menu_Item": [],
    "Serving_Size": [],
    "Calories": [],
    "Total_Fat": [],
    "Saturated_Fat": [],
    "Trans_Fat": [],
    "Cholesterol": [],
    "Sodium": [],
    "Total_Carbohydrate": [],
    "Dietary_Fiber": [],
    "Sugars": [],
    "Protein": [],
    }
    return nutritionDict

def getDHalls() -> list:
    dHalls = ["South Quad", "North Quad", "East Quad", "Bursley", "Mosher Jordan", "Twigs at Oxford", "Markley"]
    return dHalls

