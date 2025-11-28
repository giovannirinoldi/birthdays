import csv

def get_birthdays():
    with open('birthdays.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        birthdays = {}
        for row in csv_reader:
            birthdays[row[0]] = row[1]
    return birthdays

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name, birthdays):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))