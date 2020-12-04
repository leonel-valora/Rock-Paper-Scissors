import random
# Write your code here
valid_inputs = ["rock", "paper", "scissors"]
hand_shape = input()
while hand_shape != "!exit":
    if hand_shape in valid_inputs:
        msg = ""
        computer_shape = random.choice(valid_inputs)
        if (hand_shape == "rock" and computer_shape == "scissors") or (hand_shape == "paper" and computer_shape == "rock") or (hand_shape == "scissors" and computer_shape == "paper"):
            msg = "Well done. The computer chose "+ computer_shape +" and failed"
        elif hand_shape == computer_shape:
            msg = "There is a draw ("+ computer_shape +")" 
        else:
            msg = "Sorry, but the computer chose "+computer_shape
        print(msg)
    else:
        print("Invalid input")
    hand_shape = input()
print("Bye!")