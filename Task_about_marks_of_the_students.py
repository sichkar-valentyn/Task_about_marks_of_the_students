# Implementing the task
# Processing data about the student's marks
# Reading the data from the file
string = ''
average = 0
all_average_1 = 0
all_average_2 = 0
all_average_3 = 0
i = 0
with open('dataset_3363_4.txt') as inf:
    for line in inf:
        line = line.strip()
        string = line.split(';')  # Writing in the string elements divided by ';'
        # print(string)  # Checking if the string was created properly
        # Calculating the average mark for each subject for each student
        average = (int(string[1]) + int(string[2]) + int(string[3])) / 3
        print(average)
        all_average_1 += int(string[1])
        all_average_2 += int(string[2])
        all_average_3 += int(string[3])
        i += 1

# Calculating all average marks for each subject over all students
print(all_average_1 / i, all_average_2 / i, all_average_3 / i)

