# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# #print(type(data))
# #print(data["temp"].mean())
# print(data[data.temp == data.temp.max()])
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250904.csv")
grey_squirrel = (len(data[data["Primary Fur Color"] == "Gray"]))
black_squirrel = (len(data[data["Primary Fur Color"] == "Black"]))
cinnamon_squirrel = (len(data[data["Primary Fur Color"] == "Cinnamon"]))
# print(grey_squirrel)
# print(black_squirrel)
# print(cinnamon_squirrel)
data_dict = {
    "Fur color": ["Gray","Cinnamon","Black"],
    "Count": [grey_squirrel,cinnamon_squirrel,black_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv("new_squirrel_count")
