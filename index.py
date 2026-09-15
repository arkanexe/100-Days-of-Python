# print('Welcome to the band Nane Generator.')
# city = input("What\'s the name of the city you grew up in?. \n")
# pet = input("What\'s your pet name? \n")

# print('Your brand name could be ' + city + " " + pet)


# num_char = len(input('What is your name? '))
# print(f"Your name has {num_char} characters. ")
# print("Your name has " +  str(num_char) + " characters. ")

# print('Welcome to the tip calculator!')
# bill = float(input('What was the total bill? $'))

# tip = int(input('How much tip would you like to give? 10, 12 or 15? '))
# people = int(input('How many people to split the bill? '))


# total = bill + (tip / 100 * bill)

# bill_per_person = total / people

# formatiing to a must decimal places
# final_amount  = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: {final_amount}")


# Logical Operator
# print("the love calculator is calculating your score...")
# name1 = input()
# name2 = input()

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count('t')
# r = lower_names.count('r')
# u = lower_names.count('u')
# e = lower_names.count('e')

# first_digit = t + r + u + e
# l = lower_names.count('l')
# o = lower_names.count('o')
# v = lower_names.count('v')
# e = lower_names.count('e')


# last_digit = l + o + v + e

# love_score = int(str(first_digit) + str(last_digit))

# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentosl")
# elif love_score > 40 and love_score < 50:
#     print(f'Your score is {love_score} and you are alright together')
# else:
#     print(f'Your love score is {love_score}')

# import random
# random_integer = random.randint(1, 19) #random integer
# print(random_integer)

# random_float = random.random()
# print(random_float)


# states_of_america = ['Delware', 'Pennsylvania', 'New Jersey', 'Georgia']

# states_of_america.append('Lagos')
# states_of_america.extend(['Saudi'])
# print(states_of_america)


# banker roullete

# name = input().split(',')
# import random

# random_choice = random.randint(0, len(name) - 1)

# print(name[random_choice])


# treasure map
# line1 = [" ", " ", " "]
# line2 = [" ", " ", " "]
# line3 = [" ", " ", " "]
# map = [line1, line2, line3]

# print('Hiding your treasure! X marks the spot.')
# position = input()
# letter = position[0].lower()
# abc = ['a', 'b', 'c']
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[letter_index][number_index] = 'X'


# print(f'{line1}\n{line2}\n{line3}')
# fruits = ['Apple', 'Peach', 'Pear']
# for fruit in fruits:
#     print(fruit)


# student_scores = input().split()
# highest_score = 0

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

#     if student_scores[n] > highest_score:
#         highest_score = student_scores[n]

# print(f'The Highest score in the clas is: {highest_score}')
import random

mylist = ['a', 'b', 'c', 'd', 'e']
myorder = [3, 2, 0, 1, 4]
mylist = [mylist[i] for i in myorder]

print(mylist)

random.shuffle(mylist)
print(mylist)


def arkan():
    print('arkan is gonna make it in life and this akirah')

count = 0
# while count <= 10:
#     print(count)
#     count += 1

student_scores = {
    'Harry': 81,
    "Ron" : 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62
}

student_grade = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 90:
        student_grade[student] = "Outstanding"
    elif score >= 81:
        student_grade[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"

# print(student_grade)

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"]
    }
]
