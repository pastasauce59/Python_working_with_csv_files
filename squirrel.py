import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data['Primary Fur Color'])

#Getting unique values of squirrel colors from csv (for reference)
squirrel_colors = []
for color in data['Primary Fur Color']:
    if color not in squirrel_colors:
        squirrel_colors.append(color)
squirrel_colors.pop(0)
# print(squirrel_colors)

squirrel_fur_color_dict = {}
squirrel_fur_color_dict['Fur Color'] = []
squirrel_fur_color_dict['Count'] = []
for color in squirrel_colors:
    squirrel_fur_color_dict['Fur Color'].append(color)
    squirrel_fur_color_dict['Count'].append((data['Primary Fur Color'] == color).sum())
# print(squirrel_fur_color_dict)

squirrel_count_data = pandas.DataFrame(squirrel_fur_color_dict)
squirrel_count_data.to_csv('squirrel_count.csv')
