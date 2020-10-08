import random
import time
import os

#function to set number of rounds to be played. User has 3 choices. While loop doesnt move on until user has chosen a valid maximum round.
def rounds():
	bochoice=[3,5,7]
	bonum=0
	while bonum==0:
		print("Choose maximum rounds")
		for i in bochoice:
			print(i)
		bonumchoice=input("Please input your choice ")
		if bonumchoice.isalpha():
			bonum=0
			print('Try Again')
		elif int(bonumchoice) in bochoice:
			bonum=int(bonumchoice)
			print("thanks")
		else:
			bonum==0
			print("try again")
	return bonum

#Function to assign opponent hand state. Random number in range(0,3) chooses from states list
states=["rock","paper","scissors"]

def opponentstate():
	opponent=0
	a=random.randrange(0,3)
	opponent=states[a]
	return opponent

#Function to take user input to assign own hand state. Ideally I want a way to select from the choices presented without inputting a number.
def userstate():
	userchoice=[1,2,3]
	usernum=0
	while usernum==0:
		print("Make your choice!")
		for i, j in zip(states, userchoice):
			print("If you want",i,"type",j)
		userstatechoice=int(input("Choose Wisely "))
		if userstatechoice in userchoice:
			usernum=userstatechoice
			yourstate=states[usernum-1]
			print("you chose", yourstate)
		else:
			usernum=0
			print("Your choice is invalid. Try again.")
	return yourstate

#function to clear previous text
def clear():
	os.system('cls')

#function to play a round
#Idea is to use earlier functions to set user and opponent state then "resolve combat" and increase the score counter for the victor.

def playround():
	clear()
	tmprounds=rounds()
	print("We will play first to ",tmprounds)
	time.sleep(1)
	yourscore=0
	aiscore=0
	currentround=0
	clear()
	while yourscore<tmprounds and aiscore<tmprounds:
		currentround=yourscore+aiscore
		tmpuser=userstate()
		tmpopponent=opponentstate()
		print("Our contestants have locked in their choices")
		time.sleep(2)
		print("Winner of round",currentround)
		print("You",tmpuser,"\nAI",tmpopponent)
		if tmpuser==tmpopponent:
			print("Tie")
			yourscore=yourscore
			aiscore=aiscore
			print("You:",yourscore,"\nAI: ",aiscore)
			lol=input('Press Enter to continue  ')
		elif tmpuser=='rock' and tmpopponent=='scissors':
			print('You Win')
			yourscore+=1
			aiscore=aiscore
			print("You:",yourscore,"\nAI: ",aiscore)
			lol=input('Press Enter to continue  ')
		elif tmpuser=='rock' and tmpopponent=='paper':
			print('You Lose')
			yourscore=yourscore
			aiscore+=1
			print("You:",yourscore,"\nAI: ",aiscore)
			lol=input('Press Enter to continue  ')
		elif tmpuser=='paper' and tmpopponent=='rock':
			print('You Win')
			yourscore+=1
			aiscore=aiscore
			print("You:",yourscore,"\nAI: ",aiscore)
			lol=input('Press Enter to continue  ')		
		elif tmpuser=='paper' and tmpopponent=='scissors':
			print('You Lose')
			yourscore=yourscore
			aiscore+=1
			print("You:",yourscore,"\nAI: ",aiscore)
			lol=input('Press Enter to continue  ')		
		elif tmpuser=='scissors' and tmpopponent=='paper':
			print('You Win')
			yourscore+=1
			aiscore=aiscore
			print("You:",yourscore,"\nAI: ",aiscore)
			lol=input('Press Enter to continue  ')		
		elif tmpuser=='scissors' and tmpopponent=='rock':
			print('You Lose')
			yourscore=yourscore
			aiscore+=1
			print("You:",yourscore,"\nAI: ",aiscore)
			lol=input('Press Enter to continue  ')
		clear()	
	if yourscore==tmprounds:
		print("congrats you win")
	elif aiscore==tmprounds:
		print("sorry you lost")
	else:
		print('guess the programmer fucked up')
		print('thanks for playing')

playround()

#run game via rounds, set opponent state, receive user state, scorekeeping, loop until user/opponent reaches rounds required
#tmprounds=rounds()