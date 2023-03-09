import random
import easygui as eg

# Define the lists for card numbers and suits
card_numbers = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King", "Ace"]
card_suits = ["clubs", "diamonds", "hearts", "spades"]

# Function to compare the cards and return the winner
def compare_cards(player_card, computer_card):
    player_card_index = card_numbers.index(player_card)
    computer_card_index = card_numbers.index(computer_card)
    if player_card_index > computer_card_index:
        return "Player"
    elif computer_card_index > player_card_index:
        return "Computer"
    else:
        return "Tie"

# Function to get player input (play again or exit)
def get_input():
    while True:
        input_str = eg.buttonbox("Do you want to play again?", choices=["Yes", "No"])
        if input_str == "Yes":
            return True
        elif input_str == "No":
            return False

# Game loop
play_again = True
while play_again:
    # Draw random cards for player and computer
    player_card = random.choice(card_numbers)
    computer_card = random.choice(card_numbers)

    # Compare the cards and determine the winner
    winner = compare_cards(player_card, computer_card)

    # Show message box with the cards and the winner
    message = f"Player's card: {player_card}\nComputer's card: {computer_card}\n"
    if winner == "Player":
        message += "Player wins!"
    elif winner == "Computer":
        message += "Computer wins!"
    else:
        message += "It's a tie!"
    eg.msgbox(message)

    # Ask if the player wants to play again or exit
    play_again = get_input()

eg.msgbox("Thanks for playing!")
