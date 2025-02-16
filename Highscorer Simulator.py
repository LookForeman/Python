#2022-05-29

from random import randint
from time import sleep
veryNice = 69420 #nice
totalGuesses = 0

f = open("Highscore.txt", "r")
highscore = f.readline()
f.close()

highscore = int(highscore.strip()) #Removing newline
prettyHighScore = "{:,d}".format(highscore)#Turns a hard to read number into a number seperated by commas!
print("Current highscore: " + prettyHighScore)
sleep(2)


while True: #Will need to keyboard interrupt if you don't get VERY NICE.
	sleepTime = 1 #standard time to sleep
	guess = randint(0, 69420)
	totalGuesses += 1
	prettyTotalGuesses = "{:,d}".format(totalGuesses)
	print(temp, "- guess number:", prettyTotalGuesses)
	
	if guess == veryNice:
		if totalGuesses > highscore:
			highscore = totalGuesses
			f = open("Highscore.txt", "w")
			f.write(str(totalGuesses))
			f.close()
			print("New Highscore!")
			sleepTime += 1 #If you get a new highscore will add 1 second to sleeptimer
		if totalGuesses == 69420: #VERY NICE
			print("NICE.")
			break #Only way the program will naturally end
		else:
			print("Nice.")
			sleep(sleepTime)
			totalGuesses = 0
			continue
