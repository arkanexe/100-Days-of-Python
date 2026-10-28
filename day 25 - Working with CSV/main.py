# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []

#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)



# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list) / len(temp_list)

# print(average)


# print(data["temp"].max())

# print(data[data.day == 'Monday'])
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# def convert_Temp(temp):
#     return (temp * 9/5) + 32

# print(convert_Temp(monday.temp))


# data_dict  = {
#     'students': ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)

# data.to_csv("new_data.csv")

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)


data_dict = {
    "Fur Color": ['grey', 'red', 'black'],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)

df.to_csv("refined_data.csv")
