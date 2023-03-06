

import easygui
import math

# Prompt the user for inputs
school_name = easygui.enterbox("Enter the name of the school:", "School name")
max_class_size = easygui.integerbox("What is the maximum number of children allowed per class (10-30):",
                                    "Maximum class size", lowerbound=10, upperbound=30)
total_students = easygui.integerbox("What is the total number of children in the school (10-1400):",
                                     "Total number of students", lowerbound=10, upperbound=1400)
available_teachers = easygui.integerbox("How many teachers are available at {} (1-120):".format(school_name),
                                         "Actual number of teachers", lowerbound=1, upperbound=120)

# Calculate the number of classes and teachers needed
num_classes = math.ceil(total_students / max_class_size)
num_teachers_needed = num_classes
if num_teachers_needed > available_teachers:
    shortfall = num_teachers_needed - available_teachers
    easygui.msgbox("Too few teachers. You need {} more teacher/s.".format(shortfall), "Teacher shortage")
elif num_teachers_needed < available_teachers:
    excess = available_teachers - num_teachers_needed
    easygui.msgbox("Over-staffed. You have too many teacher/s. You could do without {} current teacher/s.".format(excess),
                    "Teacher excess")
else:
    easygui.msgbox("The number of teachers is correct for the number of classes.", "Teacher allocation")

# Ask whether the user wants to perform another calculation or exit
response = easygui.buttonbox("Do you want to perform another calculation?", "More calculations?", choices=["Yes", "No"])
if response == "Yes":
    # Restart the program
    exec(open(__file__).read())  # Execute the current file again
else:
    # Exit the program
    easygui.msgbox("Thanks for using this calculator. Goodbye!", "Exit")
