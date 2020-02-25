## OEFENING 3:
print('\nKIPPEN EN EIEREN \n')

from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

secretNumber = random_with_N_digits(4)
number = str(secretNumber)

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
		if numberOne == secretNumberOne :
			kip += 1
		else :
			ei += 1


	if numberTwo in array :
		if numberTwo == secretNumberTwo :
			kip += 1
		else :
			ei += 1

	if numberThree in array :
		if numberThree == secretNumberThree :
			kip += 1
		else :
			ei += 1

	if numberFour in array :
		if numberFour == secretNumberFour :
			kip += 1
		else :
			ei += 1

	if kip == 4 :
		state = True
		print('Goed gegokt zeg! Het nam je ' + str(pogingen) + ' aantal pogingen.')

	print('Je hebt ' + str(kip) + ' kippen en ' + str(ei) + ' eieren')
