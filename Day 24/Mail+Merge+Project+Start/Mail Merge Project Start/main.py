#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open("/home/ep/PycharmProjects/course/Day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("/home/ep/PycharmProjects/course/Day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in names:
    clean_name = name.strip()
    my_letter = letter.replace("[name]", clean_name)
    with open(f"./Output/ReadyToSend/letters_for_{clean_name}.docx", mode="a") as file:
        file.write(f"{my_letter}\n")

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp