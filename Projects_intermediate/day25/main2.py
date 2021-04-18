import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]
colors = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [0, 0, 0]
     }

# better solve

gray_count = len(data["Primary Fur Color"] == "Gray")
cinnamon_count = len(data["Primary Fur Color"] == "Cinnamon")
black_count = len(data["Primary Fur Color"] == "Black")

colors2 = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [gray_count, cinnamon_count, black_count]
     }
df = pandas.DataFrame(colors2)
df.to_csv("Fur_Color2.csv")
