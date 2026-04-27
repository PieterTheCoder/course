# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {student:random.randint(1, 100) for student in names}
# passed_students = {student:student_score for (student, student_score) in students_score.items() if student_score >= 60}
# print(passed_students)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)
#
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day:(temp_c * 9/5 + 32) for (day, temp_c) in weather_c.items()}
# print(weather_f)

import pandas
student_dict = {
    "student": ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'],
    "score": [67, 35, 13, 74, 92, 48]
}

# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.student)

