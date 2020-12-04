# Importing
from random import randint

# Creating functions
def getUserNames(players):
  players["player1"]["name"] = input("Player 1, please enter your name: ")
  print("Thanks and good luck!")
  players["player2"]["name"] = input("Player 2, please enter your name(If you wish to play against the computer, enter AI): ")
  print("Thanks and good luck!")

def FindPlayerName(names, playerTurn):
  if playerTurn:
    return names["player1"]["name"]
  else:
    return names["player2"]["name"]

# Create the askMove function over here. Please do it as fast as possible @MaxDubs and @Wheatenloki


# Assigning variables
# Creating the playerNames dict
playerNames = {"player1" : {"name" : "", "numWins" : 0}, "player2" : {"name" : "", "numWins" : 0}}

player1Turn = True

gameOver = False
moveCounter = 0
chipsInPile = 0
chipsTaken = 0

userChoice = 'Y'

# Opening the file to output the numMoves to later
file = open("Winners.txt", "w")

# Assigning the usernames givin
getUserNames(playerNames)
player1 = playerNames["player1"]["name"]
player2 = playerNames["player2"]["name"]

# Starting the while loop which will run while the game is in play
while userChoice == 'Y':
  # Creating the random number
  chipsInPile = randint(5, 100)

  # Printing out the amount of chips the round is going to start with
  print("The round will start with", chipsInPile, "chips in the pile")

  # Reassigning the variables so the game runs smoothly in each new round
  gameOver = False
  moveCounter = 0

  # Creating the second while loop which will have the game's contents in it
  while gameOver == False:
    # This is where you have to continue and finish the rest of the game @Sakuguy. Try to wait until askMove is done tho. Delete the break statements when you edit this area
    break
  break

# TODO #2 @MaxDubs please help @Wheatenloki finish the function askMove.
# TODO #3 @Sakuguy please write help write the main code with @whippingdot. Also solve all the problems in the code. You do half of the code and let whippingdot do the rest. The code you need to write can be reffered to from ActualChips.cpp in the int main().
# TODO #4 @whippingdot please write the main code which is there in ActualChips.cpp. The code you need to write is in the int main() fuction there.
# TODO #5 @Wheatenloki please finish defining the function askMove. Everything you need to make the function is there in ActualChips.cpp. Use that for reference.
# TODO #8 Hey, @NRafa1391 create a file on the chips branch called chips.js. Do your JS work there. I, and someone else if they want, will help you with the HTML, and if I learn CSS, then CSS too.
