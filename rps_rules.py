rock_paper_scissors_defeats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

# Your code here
for key in rock_paper_scissors_defeats:
    print(f"{key} defeats {rock_paper_scissors_defeats[key]}")