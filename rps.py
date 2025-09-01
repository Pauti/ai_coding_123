#!/usr/bin/env python3
"""
Rock-Paper-Scissors CLI Game
A best-of-3 match implementation with input validation.
"""

import random
from typing import Tuple, Optional


def get_user_choice() -> str:
    """Get and validate user input for rock, paper, or scissors."""
    valid_choices = {'rock', 'paper', 'scissors', 'r', 'p', 's'}
    choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    while True:
        choice = input("Enter your choice (rock/paper/scissors or r/p/s): ").lower().strip()

        if choice in valid_choices:
            return choice_map.get(choice, choice)

        print("Invalid choice! Please enter 'rock', 'paper', 'scissors' or 'r', 'p', 's'")


def get_computer_choice() -> str:
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice: str, computer_choice: str) -> Optional[str]:
    """
    Determine the winner of a single round.

    Args:
        user_choice: User's choice (rock/paper/scissors)
        computer_choice: Computer's choice (rock/paper/scissors)

    Returns:
        'user' if user wins, 'computer' if computer wins, None for tie
    """
    if user_choice == computer_choice:
        return None

    winning_combinations = {
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper')
    }

    if (user_choice, computer_choice) in winning_combinations:
        return 'user'
    else:
        return 'computer'


def play_round() -> Optional[str]:
    """
    Play a single round of Rock-Paper-Scissors.

    Returns:
        'user' if user wins, 'computer' if computer wins, None for tie
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner is None:
        print("It's a tie!")
    elif winner == 'user':
        print("You win this round!")
    else:
        print("Computer wins this round!")

    return winner


def play_best_of_three() -> None:
    """Play a best-of-3 match of Rock-Paper-Scissors."""
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to Rock-Paper-Scissors!")
    print("Best of 3 rounds wins the match!\n")

    while user_score < 2 and computer_score < 2:
        print(f"--- Round {round_number} ---")
        print(f"Score: You {user_score} - {computer_score} Computer")

        winner = play_round()

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Current score: You {user_score} - {computer_score} Computer\n")
        round_number += 1

    # Announce final result
    print("=" * 40)
    if user_score > computer_score:
        print("🎉 Congratulations! You won the match!")
    else:
        print("💻 Computer wins the match! Better luck next time!")
    print(f"Final score: You {user_score} - {computer_score} Computer")
    print("=" * 40)


def main() -> None:
    """Main entry point for the Rock-Paper-Scissors game."""
    try:
        play_best_of_three()

        while True:
            play_again = input("\nWould you like to play another match? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                print()
                play_best_of_three()
            elif play_again in ['n', 'no']:
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
