import csv

link = open('Exercise.csv')
csv_link = csv.reader(link)
data_lines = list(csv_link)
link_list = []
for row_num, data in enumerate(data_lines):
    link_list.append(data[row_num])

print(''.join(link_list))

# Method 2:
link_str = ''
for row_num, data in enumerate(data_lines):
    link_str += data[row_num]

print(link_str)
