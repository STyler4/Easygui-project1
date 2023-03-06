import easygui

while True:
    user_input = easygui.enterbox(
        "Enter the names of 5 places you would most like to visit\n"
        "Separate each place name with a comma")

    if user_input is None:
        exit()

    places = [p.strip() for p in user_input.split(",")]

    if len(places) != 5:
        easygui.msgbox(
            f"Sorry but you can only enter the names of 5 places and you entered {len(places)} places."
        )
    else:
        break

bullet_list = "\n".join([f"o\t{p}" for p in places])
easygui.msgbox(f"My bucket list:\n{bullet_list}", "Travel bucket list")
