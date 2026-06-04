"""Rock, Paper, Scissors, Spock, Lizard game. 
Asks user to choose between a single match, or best of 5. announces a winner after each round."""

import random
import os
import time

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

def clear_cmd():
    """Clears terminal."""
    return os.system('clear')

def prompt(message):
    """Prints an arrow before output to differentiate between user input and output."""
    print(f'---> {message}')

def greeting():
    """Prints greeting and rules of the game."""
    print("""
          WELCOME TO ROCK, PAPER, SCISSORS (+ SPOCK, LIZARD)
          The rules are as follows:

          ROCK beats scissors, lizard
          PAPER beats rock, spock
          SCISSORS beats paper, lizard
          SPOCK beats scissors, rock
          LIZARD beats spock, paper
          """)

def get_player_choice():
    """Displays acceptable options for player and asks for input. 
    Validates if input is in CHOICE_MAP and returns players choice."""
    prompt("Enter one of the following:\n\n"

           "rock/r\n"
           "paper/p\n"
           "scissors/x\n"
           "spock/s\n"
           "lizard/l\n")
    player_choice = input().lower().strip()
    clear_cmd()
    while player_choice not in CHOICE_MAP:
        prompt('Invalid entry. Try again')
        player_choice = input()
    return CHOICE_MAP[player_choice]

def get_computer_choice():
    """Returns randomized valid option."""
    computer_choice = random.choice(VALID_CHOICES)
    return computer_choice

def player_wins(player_choice, computer_choice):
    """Returns True if player selects a winning combination in WINNING_COMBOS. 
    False if otherwise"""
    return computer_choice in WINNING_COMBOS[player_choice]

def display_winner(player_choice, computer_choice):
    """Displays winner or tie based on the return value of player_wins function."""
    if player_wins(player_choice, computer_choice):
        time.sleep(.5)
        prompt('You win!')
        return 'player'
    elif player_choice == computer_choice:
        time.sleep(.5)
        prompt("It's a tie")
        return 'tie'
    else:
        time.sleep(.5)
        prompt('Computer wins')
        return 'computer'

def play_round():
    """Gets player and computer choice and invokes on display_winner(). 
    Returns 'player', 'computer' or 'tie'. """
    player_answer = get_player_choice()
    comp_answer = get_computer_choice()
    prompt(f'You chose {player_answer} and computer chose {comp_answer}')

    return display_winner(player_answer, comp_answer)

def best_of_five():
    """Initizalizes score variables for player and computer set to 0,
    followed by a while loop that initializes result to the value of play_round(). 
    uses return value of play_round() to determine which variable to increment.
    initializes winner to the user who reaches 3 points first.
    displays final score for player, computer, and announces the grand winner."""
    player_score = 0
    comp_score = 0
    winner = None
    while player_score < 3 and comp_score < 3:
        result = play_round()

        if result == 'player':
            player_score += 1
        elif result == 'computer':
            comp_score += 1

        time.sleep(.5)
        prompt(f"Player score: {player_score}, Computer score: {comp_score}")

        if player_score == 3:
            winner = 'Player'
        elif comp_score == 3:
            winner = 'Computer'
    time.sleep(.5)
    prompt(f"THE GRAND WINNER IS: {winner}")

def single_or_five():
    """Asks user to enter 1 or 5 to determine whether a single match or game of 5 will be played."""
    print("To play a single round, enter '1'\n"
      "To play best of five, enter '5'\n")
    one_or_five = input().strip()
    clear_cmd()

    while one_or_five not in ['1', '5']:
        prompt('Invalid entry. Please enter 1 or 5')
        one_or_five = input()
    
    if one_or_five == '1':
        play_round()

    elif one_or_five == '5':
        best_of_five()

greeting()
while True:
    single_or_five()
    time.sleep(1)
    prompt('Do you want to play again? (y/n)')
    answer = input().lower().strip()

    while answer not in ['y', 'n']:
        prompt("Please enter 'y' or 'n'")
        answer = input().lower().strip()

    if answer == 'n':
        break