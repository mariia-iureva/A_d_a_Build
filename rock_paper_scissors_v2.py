# complete Rock, Paper, Scissors, v2 in this code cell.

# complete game of rock, paper, scissors


def rps(player1, player2):
    """
    Rock, Paper, Scissors - v2, 
    input: player1, player2
    output: prints who is the winner 
    """

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

rps("rock","scissors")