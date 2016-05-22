import os
os.system('clear')

make = input('Enter a make: ')
model = input('Enter a model: ')
year = input('Enter a year: ')

make = make.upper()
model = model.upper()

file = open('FLAT_RCL.txt', 'r', errors = 'ignore')


