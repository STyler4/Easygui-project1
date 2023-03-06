import easygui

used_tech = easygui.enterbox("Enter the days on which you used tech\n"
                             "separate each day with a space",
                             "Days tech was used")
days = len(used_tech.split())
if days <= 3:
    easygui.msgbox(f"Congratulations, You had {days} tech free days ")
