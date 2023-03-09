"""Convert US spelling to Nz version 2
This program progresses from Spelling_convertor_v1
This program will replace ise to ize and yse to yze"""
import easygui

def convert_spelling(word):
    if "our" in word:
        word = word.replace("our", "or")
        message = f"US spelling: {word}"
    elif "ise" in word or "yse" in word:
        word = word.replace("ise", "ize").replace("yse", "yze")
        message = f"US spelling: {word}"
    else:
        message = "No change in spelling"
    return message

while True:
    user_input = easygui.enterbox("Enter a word (or 'exit' to quit): ")
    if user_input is None or user_input.lower() == "exit":
        break
    message = convert_spelling(user_input)
    easygui.msgbox(message, title="Spelling Converter Result", ok_button="OK", image=None)


