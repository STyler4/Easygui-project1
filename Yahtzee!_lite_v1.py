import random
import easygui as eg

def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

def count_dice(dice_list):
    count_dict = {}
    for dice in dice_list:
        count_dict[dice] = count_dict.get(dice, 0) + 1
    return count_dict

def check_win(dice_list):
    counts = count_dice(dice_list)
    if 5 in counts.values():
        return "Yahtzee!"
    elif 4 in counts.values():
        return "Four of a kind!"
    elif 3 in counts.values():
        return "Three of a kind!"
    else:
        return "Better luck next time"

def play_game():
    eg.msgbox("Welcome to Yahtzee Lite!")
    roll_count = 0
    dice_list = roll_dice()
    while roll_count < 2:
        msg = "You rolled: {}\nDo you want to roll again?".format(sorted(dice_list))
        choice = eg.buttonbox(msg, choices=["Roll", "Stick"])
        if choice == "Roll":
            dice_list = roll_dice()
            roll_count += 1
        else:
            result = check_win(dice_list)
            eg.msgbox("You scored: {}\n{}".format(sorted(dice_list), result))
            return
    result = check_win(dice_list)
    eg.msgbox("You scored: {}\n{}".format(sorted(dice_list), result))
    return

def main():
    play_again = True
    while play_again:
        play_game()
        choice = eg.buttonbox("Do you want to play again?", choices=["Yes", "No"])
        if choice == "No":
            play_again = False
    eg.msgbox("Thanks for playing Yahtzee Lite!")

if __name__ == "__main__":
    main()
