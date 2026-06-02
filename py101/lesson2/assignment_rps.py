"""Rock, Paper, Scissors, Spock, Lizard game. 
Asks user to choose between a single match, or best of 5. announces a winner after each round."""

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
CHOICE_MAP = {
    'r': 'rock',
    'rock': 'rock',
    'p': 'paper',
    'paper': 'paper',
    'x': 'scissors',
    'scissors': 'scissors',
    's': 'spock',
    'spock': 'spock',
    'l': 'lizard',
    'lizard': 'lizard',
}

WINNING_COMBOS = {
     'rock': ['scissors', 'lizard'],
     'paper': ['rock', 'spock'],
     'scissors': ['paper', 'lizard'],
     'spock': ['scissors', 'rock'],
     'lizard': ['spock', 'paper'],
}

def prompt(message):
    """prints an arrow before output to differentiate between user input and output"""
    print(f'---> {message}')

def get_player_choice():
    """displays acceptable options for player and asks for input. 
    Validates if input is in CHOICE_MAP and returns players choice."""
    prompt("Enter one of the following:\n\n"
           "'rock' or 'r'\n"
           "'paper' or 'p'\n"
           "'scissors' or 'x'\n"
           ";spock' or 's'\n"
           "'lizard' or 'l'\n")
    player_choice = input().lower()
    while player_choice not in CHOICE_MAP:
        prompt('Invalid entry. Try again')
        player_choice = input()

    return CHOICE_MAP[player_choice]

def get_computer_choice():
    """returns randomized valid option"""
    computer_choice = random.choice(VALID_CHOICES)
    return computer_choice

def player_wins(player_choice, computer_choice):
    """returns True if player selects a winning combination in WINNING_COMBOS. False if otherwise"""
    return computer_choice in WINNING_COMBOS[player_choice]

def display_winner(player_choice, computer_choice):
    """displays winner or tie based on the return value of player_wins function"""
    if player_wins(player_choice, computer_choice):
        prompt('You win!')
    elif player_choice == computer_choice:
        prompt("It's a tie")
    else:
        prompt('Computer wins')

def play_round():
    """gets player and computer choice and invokes on display_winner(). 
    returns 'player', 'computer' or 'tie'. """
    while True:
        player_answer = get_player_choice()
        comp_answer = get_computer_choice()

        prompt(f'You chose {player_answer} and computer chose {comp_answer}')

        display_winner(player_answer, comp_answer)

        if player_wins(player_answer, comp_answer):
            winner = 'player'
        elif player_answer == comp_answer:
            winner = 'tie'
        else:
            winner = 'computer'

        return winner

def best_of_five():
    """initizalizes score variables for player and computer set to 0,
    followed by a while loop that initializes result to the value of play_round(). 
    uses return value of play_round() to determine which variable to increment.
    initializes winner to the user who reaches 3 points first.
    displays final score for player, computer, and announces the grand winner"""
    player_score = 0
    comp_score = 0
    winner = ''
    while player_score < 3 and comp_score < 3:
        result = play_round()
        if result == 'player':
            player_score += 1
        elif result == 'computer':
            comp_score += 1

        if player_score == 3:
            winner = 'Player'
        elif comp_score == 3:
            winner = 'Computer'

    prompt(f"Player score: {player_score}")
    prompt(f"computer score: {comp_score}")
    prompt(f"THE GRAND WINNER IS: {winner}")

print("***WELCOME TO RPSSL***\n"
      "To play a single round, enter '1'\n"
      "To play best of five, enter '5'\n")
one_or_five = input()
while one_or_five not in ['1', '5']:
    prompt('Invalid entry. Please enter 1 or 5')
    one_or_five = input()
    break

while True:
    if one_or_five == '1':
        play_round()
    elif one_or_five == '5':
        best_of_five()

    prompt('Do you want to play again? (y/n)')
    answer = input().lower()

    while answer not in ['y', 'n']:
        prompt("Please enter 'y' or 'n'")
        answer = input().lower()

    if answer [0] == 'n':
        break
