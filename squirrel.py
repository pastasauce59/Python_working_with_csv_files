import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# --> Gets every gray squirrel row
# print(data[data['Primary Fur Color'] == 'Gray'])

# --> Returns True or False for a gray squirrel from every row
# print(data['Primary Fur Color'] == 'Gray')

#Getting unique values of squirrel colors from csv (for reference)
squirrel_colors = []
for color in data['Primary Fur Color']:
    if color not in squirrel_colors:
        squirrel_colors.append(color)
#To remove 'Nan' from squirrel_colors[0] and contain only actual colors
squirrel_colors.pop(0)


squirrel_fur_color_dict = {}
squirrel_fur_color_dict['Fur Color'] = []
squirrel_fur_color_dict['Count'] = []
for color in squirrel_colors:
    squirrel_fur_color_dict['Fur Color'].append(color)
    squirrel_fur_color_dict['Count'].append((data['Primary Fur Color'] == color).sum())
# print(squirrel_fur_color_dict)

squirrel_count_data = pandas.DataFrame(squirrel_fur_color_dict)
squirrel_count_data.to_csv('squirrel_count.csv')

#TESTING
