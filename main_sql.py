# return all people where age is > 10, salary > 1000
# return all unique cities where live people between age > 15 and age < 45 and salary < 5000.
# return name, surname and email of people whom salary is bigger than average salary in Spain
# will return average age people in every country.
import time
import sqlite3


def people_age(file):
    start_time = time.time()
    conn = sqlite3.connect(file)
    cursor = conn.execute("SELECT * from fake_users WHERE age > 10 AND salary > 1000")
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    conn.close()


def all_unique_cities(file):
    start_time = time.time()
    conn = sqlite3.connect(file)
    cursor = conn.execute("SELECT * from fake_users WHERE age > 10 AND age < 45 AND salary < 5000")
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    conn.close()


def bigger_than_spain(file):
    start_time = time.time()
    conn = sqlite3.connect(file)
    cursor = conn.execute("SELECT name, email from fake_users WHERE salary > (SELECT AVG(salary) FROM fake_users WHERE country = 'Spain')")
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    conn.close()


def average_age_by_country(file):
    start_time = time.time()
    conn = sqlite3.connect(file)
    cursor = conn.execute("SELECT  country, AVG(age) as 'Average age' FROM fake_users GROUP BY country;")
    elapsed_time = time.time() - start_time
    print('...::: {} sec :::...'.format(elapsed_time))
    conn.close()


def main():

    people_age("database.db")

    all_unique_cities("database.db")

    bigger_than_spain("database.db")

    average_age_by_country("database.db")


if __name__== '__main__':
    main()
