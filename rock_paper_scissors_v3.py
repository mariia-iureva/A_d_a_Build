import random

def play_again():
  """choose whether we want to play again"""
  r = random.randint(0, 1)

  return r == 0




def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"


def rps():
    """
    Rock, Paper, Scissors, 
    input: player1, player2
    output: prints who is the winner 
    """
    player1 = choose_rps()
    player2 = choose_rps()
    print(f"Player 1 choose {player1}")
    print(f"Player 2 choose {player2}\n")

    if player1 == player2:
       print("It's a tie!")
    elif player1 == 'rock':
      if player2 == 'scissors':
        print("Player 1 won!")
      else:
        print("Player 2 won!")
    elif player1 == 'paper':
      if player2 == 'rock':
        print("Player 1 won!")
      else:
        print("Player 2 won!")
    elif player1 == "scissors":
      if player2 == 'paper':
        print("Player 1 won!")
      else:
        print("Player 2 won!")
# complete the program here
print("Welcome to Rock, Paper, Scissors!\n\n-----\n")


again = True
while again:
    rps()
    print("\n-----\n")
    again = play_again()

print("Thank you for playing!")