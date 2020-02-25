## OEFENING 1:
# Draai de woorden om

# Maak een functie
def draaiOm(input) :
	inputWoorden = input.split(" ") # Verwijder alle witruimte, maak substrings
	inputWoorden = inputWoorden[-1::-1] # Draai ze om
	output = ' '.join(inputWoorden) # Voeg substrings aan elkaar toe met witruimte
	return output

input = 'Internet Of Things is much fun'	
print('\nTURNING THE WORDS! \n')
print(draaiOm(input))

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

## OEFENING 3:
print('\nKIPPEN EN EIEREN \n')

from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

secretNumber = random_with_N_digits(4)
number = str(secretNumber)
print(number)

state = False
pogingen = 0

while state == False :
	kip = 0
	ei = 0
	pogingen += 1

	print('Enter 4 digits:')
	x = raw_input()

	numberOne = x[0]
	numberTwo = x[1]
	numberThree = x[2]
	numberFour = x[3]

	secretNumberOne = number[0]
	secretNumberTwo = number[1]
	secretNumberThree = number[2]
	secretNumberFour = number[3]

	array = map(str, str(secretNumber))

	if numberOne in array :
		ei += 1

	if numberTwo in array :
		ei += 1

	if numberThree in array :
		ei += 1

	if numberFour in array :
		ei += 1

	if numberOne == secretNumberOne :
		kip += 1

	if numberTwo == secretNumberTwo :
		kip += 1

	if numberThree == secretNumberThree :
		kip += 1

	if numberFour == secretNumberFour :
		kip += 1

	if kip == 4 :
		state = True
		print('Goed gegokt zeg! Het nam je ' + str(pogingen) + ' aantal pogingen.')

	print('Je hebt ' + str(kip) + ' kippen en ' + str(ei) + ' eieren')
		

