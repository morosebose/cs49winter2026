"""
heads_up.py

Read in a list of CS related words from file and display them in 
random order one at a time on the screen until user ends the game.

Programmer: Surajit A. Bose; Date: 19 March 2026.
"""

import random

# Name of the file to read in
FILE_NAME = 'cswords.txt'

def main():
    # Get list of words in file
    word_list = get_words_from_file()

    # Get and display random word from list
    word = random.choice(word_list)
    print(word)

    # The above two lines can be combined into one:
    # print(random.choice(word_list))

    # Wait for user to hit enter for next word 
    # or to type "stop" to end the game
    choice = input()
    while choice.lower() != 'stop':
        word = random.choice(word_list)
        print(word)
        choice = input()
    
def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 

    Pre: Readable file exists at the specified path
    Post: File has been read into memory
     - List of all lines in the file is populated
    Return: List of all lines in the file
    """
    lines = []
    with open(FILE_NAME, 'r') as f:
        for line in f:
            # remove whitespace characters (\n, \t) from 
            # the start and end of the line
            line = line.strip() 
            # skip lines that have only whitespace characters 
            if line != "":
                lines.append(line)
                
    return lines

if __name__ == '__main__':
    main()