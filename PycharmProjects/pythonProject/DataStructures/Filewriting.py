myfile = open('../myfile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()

with open('../myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open('../myfile.txt', 'a') as my_new_file:
    my_new_file.write('\n This is the 4th line')
