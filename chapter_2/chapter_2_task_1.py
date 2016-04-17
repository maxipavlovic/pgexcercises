__author__ = 'Kolyubyakin Maxim'
__email__ = 'maxipavlovic@gmail.com'

'''
The “Hello, World” program is the first program you learn to write in many languages, but it doesn’t involve any input.
So create a program that prompts for your name and prints a greeting using y our name.

Example Output
What is your name? Brian
Hello, Brian, nice to meet you!

Constraint
• Keep the input, string concatenation, and output separate.

Challenges
• Write a new version of the program without using any variables.
• Write a version of the program that displays different greetings for different people.
'''


def version_1():
    name = input('What is your name? ')
    output = 'Hello, {0}, nice to meet you!'.format(name)
    print(output)


def version_2():
    print('Hello, {0}, nice to meet you!'.format(input('What is your name? ')))


def version_3():
    name = input('What is your name? ')
    if name == 'Max':
        output = 'Hello, {0}!'.format(name)
    else:
        output = 'Hello, {0}, nice to meet you!'.format(name)
    print(output)


if __name__ == '__main__':
    version_1()
    version_2()
    version_3()
