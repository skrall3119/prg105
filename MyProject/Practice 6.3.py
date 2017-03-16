def file_reader(line_number, counter, total_value):
        while line_number != '':
            value = int(line_number)
            total_value += value
            line_number = number_file.readline()
            counter += 1  # count number of times it loops
        average = (total_value/counter)  # calculate the average to simplify the print statement
        print("the average of the data is: "+format(average, '.2f'))
try:
    line = 0
    count = 0  # count number of times it loops
    total = 0  # for calculating the sum of the numbers
    number_file = open('numbers.txt', 'r')

    file_reader(line,count,total)
except ValueError:
        print("Values cannot be read! please check your file and fix any present errors.")
except IOError:
        print("Cannot find stated file.")
