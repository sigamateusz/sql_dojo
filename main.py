# return all people where age is > 10, salary > 1000
# return all unique cities where live people between age > 15 and age < 45 and salary < 5000.
# return name, surname and email of people whom salary is bigger than average salary in Spain
# will return average age people in every country.
import csv
import time


def import_file(csv_file):
    with open(csv_file, 'r') as f:
        output_list = []
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            output_list.append(line)

    return output_list[1:]


def people_age(file):
    start_time = time.time()
    output_list = []
    for row in file:
        if int(row[-1]) > 10 and int(row[-2]) > 1000:
            output_list.append(row)
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    return output_list


def all_unique_cities(file):
    start_time = time.time()
    output_list = []
    for row in file:
        if (int(row[-1]) > 15)and (int(row[-1]) < 45) and (int(row[-2]) < 5000):
            output_list.append(row[2])
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    return output_list


def bigger_than_spain(file):
    start_time = time.time()
    output_list = []
    suma = 0
    elements = 0
    for row in file:
        if row[-3] == 'Spain':
            suma += int(row[-2])
            elements += 1
    average = suma / elements

    for row in file:
        if int(row[-2]) > average:
            output_list.append([row[0], row[1]])
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    return output_list


def average_age_by_country(file):
    start_time = time.time()
    output_list = []
    countries_dict = {}
    countries = []
    for row in file:
        countries_dict[row[-3]] = [0, 0] #sum,iter
        countries.append(row[-3])
    countries = list(set(countries))
    for country in countries:
        for row in file:
            if row[-3] == country:
                countries_dict[row[-3]][0] += int(row[-1])
                countries_dict[row[-3]][1] += 1
    for key, value in countries_dict.items():
        average = value[0] / value[1]
        output_list.append([key, int(average)])
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    return output_list


def main():

    file = import_file("database.csv")

    people_age(file)

    all_unique_cities(file)

    bigger_than_spain(file)

    average_age_by_country(file)


if __name__== '__main__':
    main()