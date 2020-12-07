import random
# Write your code here
winning_cases = {
     'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
default_moves = ["rock", "paper", "scissors"]
rating_file = open("rating.txt", 'r')
# start the game
user_name = input("Enter your name: ")
print("Hello,", user_name)
declared_user_moves = input()
print("Okay, let's start")
game_move = default_moves if declared_user_moves == "" else declared_user_moves.split(",")

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
    if user_move == computer_move:
        msg = "There is a draw ("+ computer_move +")"
        user_score += 50
    elif computer_move in winning_cases[user_move]:
        msg = "Well done. The computer chose "+ computer_move +" and failed"
        user_score += 100
    return msg
    
user_move = userInput()
while user_move != "!exit":
    computer_move = random.choice(game_move)
    msg = checkWinner(user_move, computer_move)
    print(msg)
    user_move = userInput()

print("Bye!")