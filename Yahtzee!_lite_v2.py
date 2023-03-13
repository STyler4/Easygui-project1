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
        return "Yahtzee!", 50
    elif 4 in counts.values():
        return "Four of a kind!", 30
    elif 3 in counts.values():
        return "Three of a kind!", 10
    else:
        return "Better luck next time", 0


def play_game(player_name):
    eg.msgbox(f"Welcome {player_name} to Yahtzee Lite!")
    roll_count = 0
    dice_list = roll_dice()
    while roll_count < 3:
        msg = f"{player_name}, you rolled: {sorted(dice_list)}\nDo you want to roll again?"
        choice = eg.buttonbox(msg, choices=["Roll", "Stick"])
        if choice == "Roll":
            dice_list = roll_dice()
            roll_count += 1
        else:
            result, score = check_win(dice_list)
            eg.msgbox(f"{player_name}, you scored {score} points for {result}")
            return score
    result, score = check_win(dice_list)
    eg.msgbox(f"{player_name}, you scored {score} points for {result}")
    return score


def main():
    eg.msgbox("Welcome to Yahtzee Lite!")
    play_again = True
    while play_again:
        score1 = play_game("Player 1")
        score2 = play_game("Player 2")
        if score1 > score2:
            winner = "Player 1"
        elif score2 > score1:
            winner = "Player 2"
        else:
            winner = "It's a tie"
        choice = eg.buttonbox(f"{winner} won the game!\nDo you want to play again?", choices=["Yes", "No"])
        if choice == "No":
            play_again = False
    eg.msgbox("Thanks for playing Yahtzee Lite!")


if __name__ == "__main__":
    main()
