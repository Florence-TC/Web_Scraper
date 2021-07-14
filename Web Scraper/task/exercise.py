my_file = open('hyperskill-dataset-40985365.txt', 'r')
my_lines = my_file.readlines()
counter = 0
for line in my_lines:
    if line == 'summer':
        counter += 1
