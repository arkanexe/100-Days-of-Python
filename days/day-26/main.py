# new_list = [n * 2 for n in range(1, 5)]

# print(new_list)
# names = ["Adanimogo", "adam", "john", "esteher", "Roheemah", ]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(short_names, long_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [number ** 2 for number in numbers]
# print(squared_numbers)

# list_of_string = input().split(",")
# print(list_of_string)
# list_number = [int(num) for num in list_of_string]
# result = [num for num in list_number if num % 2 == 0]

# print(result)


# with open("file1.txt") as file1, open("file2.txt") as file2:
#     data1 = [line.strip() for line in file1.readlines()]
#     data2 = [line.strip() for line in file2.readlines()]



# combined_data = [data for data in data1 if data in data2]

# print(combined_data)
# names = ["alex", "beth", "caroline", 'dave', 'eleanor', 'freddie']
# import random

# student_scores = {student:random.randint(1, 100) for student in names}

# passed_student = {student : score for (student, score) in student_scores.items() if score > 60}

# print(student_scores)
# print(passed_student)


# sentence = input().split()

# diction = {word: len(word) for word in sentence}

# print(diction)

# weather_c = eval(input())

# def convert(degree):
#     return (int(degree) * 9 / 5) + 32

# weather_f = {day: convert(weather)  for (day, weather) in weather_c.items()}

# print(weather_f)

# student_dict = {
#     "student" : ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (index, row) in student_data_frame.iterrows():
#     print(row.score , index)

file = pandas.read_csv("alphabet.csv")
code_name = {code.letter: code.code for (index, code) in file.iterrows()}

print(code_name)

word = input("Enter a word: ").upper()

new_word = [code_name[letter] for letter in word]

print(new_word)
