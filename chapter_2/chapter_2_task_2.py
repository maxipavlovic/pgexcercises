from tkinter import *

__author__ = 'Kolyubyakin Maxim'
__email__ = 'maxipavlovic@gmail.com'

'''
Create a program that prompts for an input string and displays output that shows the input string
and the number of characters the string contains.

Example Output
What is the input string? Homer
Homer has 5 characters.

Constraints
• Be sure the output contains the original string.
• Use a single output statement to construct the output.
• Use a built-in function of the programming language to determine the length of the string.

Challenges
• If the user enters nothing, state that the user must enter something into the program.
• Implement this program using a graphical user interface and update the character counter every time a key is pressed.
If your language doesn’t have a particularly friendly GUI library,
try doing this exercise with HTML and JavaScript instead.
'''


NO_INPUT = 'Please, input something!'


def callback(e_s, l_s):
    line = e_s.get()
    if not line:
        l_s.set(NO_INPUT)
    else:
        l_s.set('{0} has {1} characters.'.format(line, len(line)))

if __name__ == '__main__':
    gui = Tk()
    entry_string, label_string = StringVar(), StringVar(value=NO_INPUT)
    entry_string.trace("w", lambda name, index, mode, sv=entry_string: callback(entry_string, label_string))
    Label(gui, text='What is the input string?').grid(row=0)
    Label(gui, textvariable=label_string).grid(row=1)
    entry = Entry(gui, textvariable=entry_string).grid(row=0, column=1)

    mainloop()
