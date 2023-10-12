import csv

data = open('example.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)
print(len(data_lines))
for line in data_lines[5]:
    print(line)
# all_emails = []
# for line in data_lines[1:]:
#     all_emails.append(line[3])

# print(all_emails)

full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + " " + line[2])

print(full_names)

file_to_write = open("to_save_file.csv", mode='w', newline='')
csv_writer = csv.writer(file_to_write)
csv_writer.writerow(['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city'])
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

csv_writer.writerow([all_emails])
