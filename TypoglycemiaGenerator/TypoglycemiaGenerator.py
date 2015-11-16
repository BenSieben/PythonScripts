"""
Takes an input text file and prints out a similar
version that has been modified according to the rules
of typoglycemia, where humans are capable of reading
words even if the inside letters are in the wrong order
"""
import random


#  Function to read the contents of either the default text file or default text file, depending on user input
def read_text(use_default):
    if use_default:
        with open("typoglycemiaInput.txt") as txt:
            return_text = txt.read()
    else:
        if len(filename) > 0:
            with open(filename) as txt:
                return_text = txt.read()
        else:
            return read_text(True)
    return return_text


#  Function to randomize the input word according to the rules of typoglycemia
def randomize_word(word):
    length = len(word)
    if len <= 3:  # If the word is 3 or less characters long, the word cannot be shuffled around at all
        scrambled_word = word
    else:

    scrambled_word = ""
    return scrambled_word

filename = input("Enter the directory that you would like to generate a typoglycemia version of" +
                 " (leave blank to use default typoglycemiaInput.txt")

text = read_text(filename)

textWords = text.split()  # Obtain an array of the words inside the text string

for w in textWords:
    print(w, len(w))

print(text)
