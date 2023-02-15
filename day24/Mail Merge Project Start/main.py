#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    with open("Input/Letters/starting_letter.txt", mode="r") as letter:
        x = letter.read()
        out = x.replace("[name]", name.strip())
        path = "Output/ReadyToSend/"
        with open(f"{path}{name}.txt", mode="w") as output:
            output.write(out)

#actual solution code:
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("./Input/Letter/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open("./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w') as completed_letter:
            completed_letter.write(new_letter)
"""



