import random

def get_user_choice():
    choice = input("Choose one: Rock (r), Paper (p), or Scissors (s): ").lower()
    while choice not in ['r', 'p', 's']:
        choice = input("Invalid choice! Choose again: ").lower()
    return choice

def get_computer_choice():
    choice = random.choice(['r', 'p', 's'])
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}")
    print(f"The computer chose {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()
 