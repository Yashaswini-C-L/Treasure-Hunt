print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Which direction would you like to choose? Right or left? ")
if direction == "Left" or direction == "left":
    print("Congrats, you have reached the bank of the river.")
    wait_swim = input("Would you like to Wait in the bank of the river or Swim across it? ")
    if wait_swim == "wait" or wait_swim == "Wait":
        print("Your boat has arrived, You can take the boat.")
        colours = input("Choose a colour, Red or Yellow or Blue ")
        if colours == "Red" or colours == "red":
            print("Sorry:(( You burnt into ashes. The game ended.")
        elif colours == "Yellow" or colours == "yellow":
            print("Congrats! You won the game.")
        else:
            print("Oops...you drowned. The game ended.")
    else:
        print("Oops...You are attacked by a crocodile. The game ended.")
else:
    print("Sorry, you fell into a well. The game ended.")

