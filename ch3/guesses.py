color='blue'
guess=''
guesses=0


while guess!=color:
	guess = input('What color am I thinking of? ')
	guesses = guesses+1
if guesses==1:
	print('It took you 1 guess')
else:
	print('It took you', guesses, 'guesses')