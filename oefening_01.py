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