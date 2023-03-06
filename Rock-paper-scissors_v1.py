import random
import easygui

# Define a list of weapons
weapons = ['rock', 'paper', 'scissors']

# Display welcome message and rules
easygui.msgbox("Welcome to Rock-Paper-Scissors! \nRock beats scissors, paper beats rock, and scissors beats paper.")

play_again = True
while play_again:
    # Get the user's choice of weapon using a buttonbox
    user_weapon = easygui.buttonbox("Choose your weapon:", choices=weapons)

    # Generate the computer's random choice of weapon
    computer_weapon = random.choice(weapons)
    easygui.msgbox("The computer chose " + computer_weapon + ".")

    # Determine the winner
    if user_weapon == computer_weapon:
        easygui.msgbox("It's a tie!")
    elif user_weapon == 'rock' and computer_weapon == 'scissors':
        easygui.msgbox("You win! Rock beats scissors.")
    elif user_weapon == 'paper' and computer_weapon == 'rock':
        easygui.msgbox("You win! Paper beats rock.")
    elif user_weapon == 'scissors' and computer_weapon == 'paper':
        easygui.msgbox("You win! Scissors beats paper.")
    else:
        easygui.msgbox("Sorry, you lose!")

    # Ask the user if they want to play again
    play_again = easygui.ynbox("Do you want to play again?", "Play again?")
