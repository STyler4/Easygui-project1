import easygui

# Prompt the user to enter their top three places to visit
places_to_visit = []
for i in range(3):
    place = easygui.enterbox("Enter your #" + str(i + 1) + " choice for a place to visit:")
    places_to_visit.append(place)

# Display the output using easygui message boxes
easygui.msgbox("The place I would most like to visit is " + places_to_visit[0] + ".")
easygui.msgbox("My second choice would be " + places_to_visit[1] + ".")
easygui.msgbox("My third choice for places to visit is " + places_to_visit[2] + ".")
