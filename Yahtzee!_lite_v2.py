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

if __name__ == "__main__":
    main()


