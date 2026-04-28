# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
Nato_DF = pandas.DataFrame(file)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alpha_stands_for = {index:row for (index, row) in Nato_DF.iterrows()}
print(alpha_stands_for)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
text = input("Write a word").upper()
list_of_code = [alphabet for alphabet in text ]
print(list_of_code)
