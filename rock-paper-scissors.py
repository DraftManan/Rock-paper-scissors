import random

def play(player):
    m = ("r", "p", "s")
    computer = m[random.randrange(len(m))]
    if player == computer:
       result = "tie"
    elif player == "r" and computer == "s":
       result = "you win"
    elif player == "p" and computer == "r":
       result = "you win"
    elif player == "s" and computer == "p":
       result = "you win"
    else: 
       result = "you lose"
    print("you: {} <=> computer: {} => {}". format(player, computer, result))

while True:
    player = input("[r]ock, [p]aper, [s]cissors, e[x]it")
    if player == "x":
       break 
    else:
       play(player)