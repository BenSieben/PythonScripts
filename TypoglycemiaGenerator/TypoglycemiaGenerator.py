"""
Takes an input text file and prints out a similar
version that has been modified according to the rules
of typoglycemia, where humans are capable of reading
words even if the inside letters are in the wrong order
"""
import random
import string


#  Function to read the contents of either the default text file or default text file, depending on user input
def read_text(filename):
    if len(filename) <= 0:
        with open("typoglycemiaInput.txt") as txt:
            return_text = txt.read()
    else:
        with open(filename) as txt:
            return_text = txt.read()
    return return_text


# Helper method for randomize_word that mixes up characters in the input word
def mix_word(word):
    mixed_word = []
    for character in word:
        mixed_word.append(character)
    random.shuffle(mixed_word)
    return "".join(mixed_word)


#  Function to randomize the input word according to the rules of typoglycemia
def randomize_word(word):
    if len(word) <= 3:  # If the word is 3 or less characters long, the word cannot be shuffled around at all
        scrambled_word = word
    elif word.isnumeric(): # Do not scramble numbers
        scrambled_word = word
    else:
        start_index = 1
        end_index = len(word) - 1
        while word[start_index] in string.punctuation:
            start_index += 1
        while word[end_index] in string.punctuation:
            end_index -= 1
        mixed_word = mix_word(word[start_index:end_index])
        scrambled_word = word[:start_index] + mixed_word + word[end_index:]
    return scrambled_word


filename_input = input("Enter the directory that you would like to generate a typoglycemia version of" +
                       " (leave blank to use  the default typoglycemiaInput.txt):\n")

text = read_text(filename_input)

split_text = text.split()  # Obtain an array of the words inside the text string

modified_text = []
for w in split_text:
    modified_text.append(randomize_word(w))

print("Original Text:\n" + text + "\n")
print("Modified Text:\n" + " ".join(modified_text))
