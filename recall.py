import os
os.system('clear')

make = input('Enter a make: ')
model = input('Enter a model: ')
year = input('Enter a year: ')

make = make.upper()
model = model.upper()

file = open('FLAT_RCL.txt', 'r', errors = 'ignore')

if make == "":
	print("Please enter a valid make, model, and year.")
if model == "":
	print("Please enter a valid make, model, and year.")
if year == "":
	print("Please enter a valid make, model, and year.")

for line in file:
	x = line.split("\t")
	if x[2] == make and x[3] == model and x[4] == year:
		print (x[6], x[21])
		print ('\n')
