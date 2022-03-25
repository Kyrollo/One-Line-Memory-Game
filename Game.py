import random               #Name: Kerollos Mansour Milad
import os                   #ID: 20210305       #Game 5
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
char_1 = list(random.choices(alphabet, k=10))       #Take 10 random characters
char_2 = char_1*2        #Repeat every character twice 
random.shuffle(char_2)   #Shuffle the elements in the list

def game(score):
    num1 = int(input("Write the first number "))
    num2 = int(input("Write the second number "))   #Take the two numbers from the players
    if num1 == num2:    #When the player put same numbers
        print("Please choose two different numbers")
        num1 = int(input("Write the first number "))
        num2 = int(input("Write the second number "))

    if char_2[num1] == char_2[num2]:         #Cover th position by Asterisk when two characters match
        char_2[num1] = "*"
        char_2[num2] = "*"
        score += 1      #Calculate the score
    for i in range(len(char_2)):        #Prints the position and asterisk
        if i == num1 or i == num2:
          print(char_2[i], end = " ")
        elif char_2[num1]==char_2[num2]:
            print(char_2[i], end = " ")
        else:
            print(i, end = " ")
    return score

turn = True
player_1 = 0
player_2 = 0        #Score of the two players

print("--Welcome to Line Memory Game--") 
coices_2 = str(input("Do you know the rules of game line memory? yes/no ")) #print the rules if yhe user doesn't know
if (coices_2.upper() == "NO") or (coices_2.upper() == "N") or (coices_2.upper() == "NOPE") or (
        coices_2.upper() == "NOP"):
    print("1- Every player choose a two numbers between 0 and 19")
    print("2- If the character position of number you input are same, your take one point")
    print("3- The player who has most points win")
elif (coices_2.upper() == "YES") or (coices_2.upper() == "Y") or (coices_2.upper() == "YEAH") or (
        coices_2.upper() == "YUP"):
    pass

while char_2.count("*")!=len(char_2):       #Loop until all characters will asterisk
    if turn:
        print("\n--First player rule--")        #Turn of the first player
        player_1 = game(player_1)               #Start first player's turn
        turn = False
    else:
        print("\n--Second player rule--")
        player_2 = game(player_2)
        turn = True
    os.system("pause")              #Pause the terminal
    os.system("cls")                #Clear the screen

if player_1 > player_2:             #print the result
   print("\n--Player 1 won--")     
elif player_2 > player_1:
    print("\n--Player 2 won--")
else:
    print("\n--Draw--")  