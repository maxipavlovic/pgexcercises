__author__ = 'Kolyubyakin Maxim'
__email__ = 'maxipavlovic@gmail.com'

'''
Quotation marks are often used to denote the start and end of a string.
But sometimes we need to print out the quotation marks themselves by using escape characters.
Create a program that prompts for a quote and an author.
Display the quotation and author as shown in the example output.

Example Output
What is the quote? These aren't the droids you're looking for.
Who said it? Obi-Wan Kenobi
Obi-Wan Kenobi says, "These aren't the droids you're looking for."

Constraints
• Use a single output statement to produce this output, using appropriate string-escaping techniques for quotes.
• If your language supports string interpolation or string substitution, don’ t use it for this exercise.
Use string concatenation instead.

Challenge
• Modify this program so that instead of prompting for quotes from the user,
you create a structure that holds quotes and their associated attributions and then display
all of the quotes using the format in the example. An array of maps would be a good choice.
'''


def version_1():
    quote = input('What is the quote? ')
    name = input('Who said it? ')
    print(name + ' says, "' + quote + '"')


def version_2():
    quote = {
        'Obi-Wan Kenobi': [
            "These aren't the droids you're looking for."
        ],
        'Any': [
            "Hey",
            "Ya"
        ]
    }
    name = input('Who said the quote? ')
    if name in quote:
        for q in quote[name]:
            print(name + ' says, "' + q + '"')
    else:
        print(name + ' says nothing.')


if __name__ == '__main__':
    version_1()
    version_2()