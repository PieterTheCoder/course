# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")

# """Will print out DataFrame which is the table of a column"""
# print(type(data))
# """Will print out Series which is a column"""
# print(type(data["temp"]))
# """From DataFrame Will convert it to a dictionary"""
# data_dict = data.to_dict()
# """From Series WIll convert it to a list"""
list_of_temp = data["temp"].to_list()
# print(len(list_of_temp))

# average = sum(list_of_temp) / len(list_of_temp)
# print(average)
# print(data["temp"].mean())

# series_of_temp = pandas.Series(list_of_temp)
# print(series_of_temp.max())
# print(data["temp"].max())

#Get data in column
# print(data["condition"])
# print(data.condition)

#Get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

#Get Data from any condition
# monday = data[data.day == "Monday"]
# temp_of_monday = monday.temp[0]
# monday_temp_F = temp_of_monday * 9/5 + 32
# print(monday_temp_F)

data_dict = {
    "Name": ["Josephan", "Aji", "Yosua", "Kaleb", "Zelig", "Otniel", " Kristo", "Ezra", "Darrel", "Zhandy"],
    "Scores": [82, 85, 90, 83, 79, 80, 73, 81, 71, 53]
}
dictionary_of_data = pandas.DataFrame(data_dict)
print(dictionary_of_data)