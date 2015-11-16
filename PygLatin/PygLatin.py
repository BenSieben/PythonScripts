"""
Takes in a word as input
and converts it to Pig Latin

This is an exercise from Codecademy
"""

pyg = 'ay'

original = input('Enter a word:') # Tells Python to take in user input and store it in the variable "original"

if len(original) > 0 and original.isalpha():  # Make sure the input is only letters and at least one letter long
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    # The word[1:len(word)] is called a splice and is used to extract a specific portion of the word.
    # Syntax is <string>[<start index>:<end (exclusive) index>:<collection pattern>]
    # Pattern negative means go backwards, and number means how many characters to skip before taking the next character
    # Default collection pattern is 1 and does not have to be indicated in the splice
    print(new_word)
else:
    print('empty')
