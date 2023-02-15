# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
# import pandas
import pandas as pd
data = pd.read_csv("weather_data.csv")
# print(type(data))   # this is a pandas dataframe, tabular structure or 2D data is dataframe
# print("\n")
# print(type(data['temp']))   # this is a pandas series, series data or 1D data is series, equivalent to list

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

# print(data.mean(0))
print(data.temp.mean())
print(data[data.day == 'Monday'])
monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

#Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Tanish"],
    "scores": [76, 56, 65]
}

scratch = pd.DataFrame(data_dict)
scratch.to_csv("New_data.csv")