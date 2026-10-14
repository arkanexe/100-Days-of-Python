# reading...

# with open("index.txt") as file:
#     contents = file.read()
#     print(contents)


# writing
# with open("my_file.txt", mode = "w") as file:
#     file.write("New text.")


PLACEHOLDER = "[name]"

names = ["Ayanbisi", "Yemi", "Kola", "Femi", "Shola"]

with open("./starting_letter.txt") as file:
    letter_contents = file.read()
    for name in names:
        new_letters = letter_contents.replace(PLACEHOLDER, name)
        with open(f"letters/letter_for_{name}.txt", mode="w") as letter:
            letter.write(new_letters)
