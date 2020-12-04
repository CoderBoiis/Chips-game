class player:
  name = ""
  numWins = 0

def getUserNames(players):
  players[0] =  input("Player 1, please enter your name: ")
  print("Thanks and good luck!")
  players[1] = input("Player 2, please enter your name(If you wish to play against the computer, enter AI): ")
  print("Thanks and good luck!")

def FindPlayerName(names, playerTurn):
  if playerTurn:
    return names[0]
  else:
    return names[1]

# TODO #2 @MaxDubs please help @Wheatenloki finish the function askMove.
# TODO #3 @Sakuguy please write help write the main code with @whippingdot. Also solve all the problems in the code. You do half of the code and let whippingdot do the rest. The code you need to write can be reffered to from ActualChips.cpp in the int main().
# TODO #4 @whippingdot please write the main code which is there in ActualChips.cpp. The code you need to write is in the int main() fuction there.
# TODO #5 @Wheatenloki please finish defining the function askMove. Everything you need to make the function is there in ActualChips.cpp. Use that for reference.
# TODO #8 Hey, @NRafa1391 create a file on the chips branch called chips.js. Do your JS work there. I, and someone else if they want, will help you with the HTML, and if I learn CSS, then CSS too.
