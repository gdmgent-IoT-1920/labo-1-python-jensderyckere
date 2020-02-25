# OEFENING 2:
# Lees een txt-file

file = open("namen.txt", "r")
# print(file.read())

num_names = 0
num_frederick = 0
num_olivier = 0
num_evelien = 0

with open("namen.txt", "r") as f:
	for line in f:
		names = line.split()

		num_names += len(names)
		name = '\n'.join(names)

		if name == 'Frederick' :
			num_frederick += 1
		
		if name == 'Olivier' :
			num_olivier += 1
		
		if name == 'Evelien' :
			num_evelien += 1

# Amount of the names
print('\nCOUNTING THE NAMES! \n')
print('Hoeveelheid aan Frederick = ' + str(num_frederick))
print('Hoeveelheid aan Evelien = ' + str(num_evelien))
print('Hoeveelheid aan Olivier = ' + str(num_olivier))