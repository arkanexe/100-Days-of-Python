# try:
#     file  = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist. ")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")

#     raise TypeError("This is an error i made up. ")


# height = float(input("height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human should not be over 3 metres")


# fruits = eval(input())
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie ")
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " Pie")


facebook_posts =  [
    {"likes": 21, 'comments':  2},
    {"likes": 21, 'comments':  2},
    {"likes": 21, 'comments':  2},
    {"share": 21, 'comments':  2}
]


total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["likes"]
    except KeyError:
        pass
else:
        print(total_likes)
