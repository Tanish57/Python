
import pandas

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")

NATOdict = {row.letter:row.code for (index, row) in data.iterrows()}
print(NATOdict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Please enter a word: ").upper()
output = [NATOdict[letter] for letter in user]
print(output)

