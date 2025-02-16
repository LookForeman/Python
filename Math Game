# Date: 2017-12-27
# Updated: 2021-11-11
# Math Game
import random

allowableDifficulty = ("1", "2", "3", "4")
allowableGameMobde = ("1", "2", "3", "4", "5")
exitCommands = ("Exit", "Exit.", "exit", "exit.", "EXIT", "EXIT.", "Quit", "Quit.", "Stop", "Stop.")


def difficulty(c):
	
	if c == "1":
		a = random.randrange(10)
		b = random.randrange(10)
	elif c == "2":
		a = random.randrange(25)
		b = random.randrange(25)
	elif c == "3":
		a = random.randrange(50)
		b = random.randrange(50)
	elif c == "4":
		a = random.randrange(100)
		b = random.randrange(100)
	else:
		raise NameError
	
	return a,b

while True:
	try:
		diff = str(input("\n\nPlease enter a difficulty:\n\n1. Easy\n2. Normal\n3. Hard\n4. Insane\n"))
		if diff not in allowableDifficulty:
			raise NameError
		break
	except:
		print("\nError. Incorrect input. Please try again.\n")


while True:
	

	
	try:
		mode = str(input("\nWelcome to the Math Game. Choose a game mode:\n1. Add\n2. Subtract\n3. Divide\n4. Multiply\n5. Exit\n\n"))
		if mode == "1":
			while True:
				a,b =  difficulty(diff)
				answer = a + b
				user_input = int(input("What is %d + %d?\n" % (a,b)))
				if answer == user_input:
					print("\nCorrect!\n")
				
				else:
					print("Incorrect! The answer was: %s!\n" % answer)
				user_input = str(input("\nContinue? Type no to quit.\n"))
				if user_input.lower() == "no":
					break
		elif mode == "2":
			while True:
				a,b =  difficulty(diff)
				answer = a - b
				user_input = int(input("What is %d - %d?\n" % (a,b)))
				if answer == user_input:
					print("\nCorrect!\n")
				
				else:
					print("Incorrect! The answer was: %s!\n" % answer)
				user_input = str(input("\nContinue? Type no to quit.\n"))
				if user_input.lower() == "no":
					break
		elif mode == "3":
			while True:
				a,b =  difficulty(diff)
				if b == 0:
					b = random.randrange(1, 10)
				answer = a // b
				user_input = int(input("What is %d // %d?\n" % (a,b)))
				if answer == user_input:
					print("\nCorrect!\n")
				
				else:
					print("Incorrect! The answer was: %s!\n" % answer)
				user_input = str(input("\nContinue? Type no to quit.\n"))
				if user_input.lower() == "no":
					break
		elif mode == "4":
			while True:
				a,b =  difficulty(diff)
				answer = a * b
				user_input = int(input("What is %d * %d?\n" % (a,b)))
				if answer == user_input:
					print("\nCorrect!\n")
				
				else:
					print("Incorrect! The answer was: %s!" % answer)
				user_input = str(input("\nContinue? Type no to quit.\n"))
				if user_input.lower() == "no":
					break
		elif mode == "5" or mode in exitCommands:
			print("\nThanks for playing! Goodbye.\n")
			break
		else:
			print("\nError. Incorrect input. Please try again.")
		
	except NameError:
		print("Name Error")
	except ValueError:
		print("Value Error")
	except:
		print("Error")
	
