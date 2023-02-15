import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray)
print(black)
print(cinnamon)

data_dict = {
    "Fur_Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray, black, cinnamon]
}

print((data_dict))

fur_color = pd.DataFrame(data_dict)
fur_color.to_csv("Fur_color.csv")