import random
# Write your code here
game_move = ["rock", "paper", "scissors"]
rating_file = open("rating.txt", 'r')
# start the game
user_name = input("Enter your name: ")
print("Hello,", user_name)

def initUserScore(user, file):
    score = 0
    for line in file:
        if user in line:
            user, score = line.split()
            score = int(score)
            break;
    return score

user_score = initUserScore(user_name, rating_file)

def userInput():
    option = input()
    while option not in game_move and option != "!exit":
        if option == "!rating":
            print("Your rating:", user_score)
        else:
            print("Invalid input")
        option = input()
    return option
     
def checkWinner(user_move, computer_move):
    global user_score
    msg = "Sorry, but the computer chose "+computer_move
    if (user_move == "rock" and computer_move == "scissors") or (user_move == "paper" and computer_move == "rock") or (user_move == "scissors" and computer_move == "paper"):
        msg = "Well done. The computer chose "+ computer_move +" and failed"
        user_score += 100
    elif user_move == computer_move:
        msg = "There is a draw ("+ computer_move +")"
        user_score += 50
    print(user_score)
    return msg
    
user_move = userInput()
while user_move != "!exit":
    computer_move = random.choice(game_move)
    msg = checkWinner(user_move, computer_move)
    print(msg)
    user_move = userInput()

print("Bye!")
    