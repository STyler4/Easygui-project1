"""Convert US spelling to Nz version 2
This program progresses from Spelling_convertor_v1
This program will replace ise to ize and yse to yze"""
import easygui

nz_word = easygui.enterbox("Please enter the NZ word", "Word to check")
letters = list(nz_word)
letters.remove("u")
easygui.msgbox(f"The American spelling of {nz_word} is {''.join(letters)}",
               f"Results")

