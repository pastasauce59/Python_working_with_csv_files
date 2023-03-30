# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # print(data)
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data['temp'])

data_dict = data.to_dict()
# print(data_dict)

#Getting data from columns
temp_list = data['temp'].to_list()
# OR CAN USE 'data.temp' without brackets
# print(temp_list)

# Getting average calculated temperature
avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

### OR - using pandas

# print(data['temp'].mean())


#Getting MAX value from temperatures list
# print(data['temp'].max())


#Getting data in a row
# print(data[data.day == 'Monday'])

#Printing the row of data which had the highest temperature
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


#Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
# print(new_data)
new_data.to_csv('new_data.csv')