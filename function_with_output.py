# # def format_name(f_name, l_name):
# #     formated_f_name = f_name.title()
# #     formated_l_name = l_name.title()
# #     return f"{formated_f_name} {formated_l_name}"

# # name = input("enter your name ").split()
# # print(*name)
# # print(format_name(*name))


# # person = {
# #     "name": "John",
# #     "age": 25
# # }

# # for key, value in person.items():
# #     print(key, value, sep = "#")
# # names = ["John", "Mary", "Alex"]
# # for i, name in enumerate(names, start=1):
# #     print(i + 1, name, end=f" that line {i + 1} \n")

# # for number in range(5):
# #     print(number)
# # else:
# #     print("Loop finished")

# # names = ["John", "Mary", "Alex"]
# # ages = [20, 25, 30, 48]

# # for name, age in zip(names, ages):
# #     print(name, age)

# # for i in range(2, 6):
# #     print(i)


# for n in range(6):
#     if n == 2:
#         break
#     print(n)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers = [number * 2 for number in numbers]
# print(numbers)


# for row in range(6):
#     for column in range(row):
#         print("*", end="")
#     print("*")


# for number in range(1,6):
#     for num in range(1, number):
#         print(num, end="")
#     print()

# def square(number):
#     """Take number into a square"""
#     return number ** 2

# # inputNumber = int(input("enter a number: "))
# # print(square(inputNumber))



# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }


# still_calculating = True
# num1 = int(input("What's the first number?: "))

# while still_calculating:
#     operation = input("Pick an operation: ")
#     num2 = int(input("What the next number?: "))

#     result = operations[operation](num1, num2)

#     tocontinue = input(f"Type y to continue with {result} or start new calculation")
#     num1 = result

#     if tocontinue == "n":
#         still_calculating = False


# Password Strenght

# def password_checker(password):
#     if len(password) < 8:
#         return "Not up to 8 characters"

#     isdigit = False
#     islower = False
#     istitle = False

#     for letter in password:
#         if letter.isdigit():
#             isdigit = True
#         if letter.islower():
#             islower = True
#         if letter.istitle():
#             istitle = True

#     if isdigit and islower and istitle:
#         return f"{password} is certified"
#     else:
#         return "neeed checks"


# password = input("check your password : ")

# password_result = password_checker(password)

# print(password_result)


# number = int(input("what the row ? "))

# for row in range(1, number + 1):
#     for column in range(1, row + 1):
#         print(column, end=" ", sep=",")
#     print()


students = int(input("How many students? "))
school = {}

for student in range(students):
    name = input("Student name: ")
    score = int(input("Student score: "))

    school[name] = score


print(school)

def grader(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"



highest_score = 0

first_key = next(iter(school))       # Get first key
lowest_score = school[first_key]      # Get its value
student_passed = 0
student_failed = 0

avg_score = 0

for name, score in school.items():

    print(f"{name}: {score} - {grader(score)}")

    avg_score += score

    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

    if score >= 60:
        student_passed += 1
    else:
        student_failed += 1

print(f"Highest score: {highest_score}")
print(f"lowest score: {lowest_score}")
print(f"Average score: {avg_score / len(school)}")
print(f"Student Passed: {student_passed}")
print(f"student failed: {student_failed}")
