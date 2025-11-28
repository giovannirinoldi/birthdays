#! /usr/bin/env python3
import argparse

from birthdays import return_birthday, get_birthdays
birthdays = get_birthdays()
names: list  = []
surnames: list = []
for i in birthdays.keys():
    names.append(i.split(' ')[0])
    surnames.append(i.split(' ')[1])

parser = argparse.ArgumentParser()
parser.add_argument('-name', type = str, choices = names)
parser.add_argument('-surname', type = str, choices = surnames)
args = parser.parse_args()

return_birthday(args.name + ' ' + args.surname, birthdays)