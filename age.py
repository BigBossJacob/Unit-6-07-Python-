myAge = 15
myGuess = int(input("Try to guess my age: "))

while myAge != myGuess:
	if myGuess > myAge:
		print ("I'm younger than this! Try again!")
		myGuess = int(input("Try to guess my age: "))

	if myGuess < myAge: 
		print ("I'm older than this! Try again!")
		myGuess = int(input("Try to guess my age: "))
		
	if myGuess == myAge:
		print ("You guessed my age!")
		break
			 