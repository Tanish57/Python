
import pandas

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")

NATOdict = {row.letter:row.code for (index, row) in data.iterrows()}
print(NATOdict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user = input("Please enter a word: ").upper()
    try:
        output = [NATOdict[letter] for letter in user]
    except KeyError:
        print("Sorry! only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()
