import random

# word_list = ['ardvark', 'baboon', 'camel']

# chosenWORD = random.choice(word_list)

# end_of_game = False

# display = []
# for letter in chosenWORD:
#      display += "_"

# lives = 6
# while not end_of_game:
#      guess = input("Guess a letter: ").lower()
#      for position in range(len(chosenWORD)):
#           if guess == chosenWORD[position]:
#                display[position] = guess

#      if guess not in chosenWORD:
#           lives -= 1
#           if lives == 0:
#                end_of_game = True
#                print("You Lose.")
#      print(f"{' '.join(display)}")
#      if "_" not in display:
#           end_of_game = True
#           print('You Win.')
# Function that allows for input
def greet_with_name(name):
     print(f"Hello {name}")

# greet_with_name("Arkan")
# Math method
# def prime_checker(number):
#      isPrime = True
#      for n in range(2, number):
#           print(n)
#      #      if number % n == 0:
#      #           isPrime = False
#      # if isPrime:
#      #      print("It's a prime number")
#      # else:
#      #      print("It's not a prime number")


# n = int(input())
# prime_checker(n)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_again = True

def cipher(cipher_direction, plain_text, shift_amount):
     cipher_text = ""
     if cipher_direction == "decode":
           shift_amount *= -1

     for letter in plain_text:
          if letter in alphabet:
               position = alphabet.index(letter)
               new_position = position + shift_amount

               if new_position >= len(alphabet):
                    new_position = new_position - len(alphabet)

               cipher_text += alphabet[new_position]
          else:
               cipher_text += letter

     print(f"The {cipher_direction}d text is {cipher_text}")

while run_again:

     direction = input("Type the 'encode' to encrypt, type 'decode' to decrypt: \n")
     text = input("Type your message: \n").lower()
     shift = int(input("Type the shift number: \n"))
     cipher(direction, text, shift)

     condition = input(f"Type 'yes' if you want to go again. otherwise type 'no' \n").lower()

     if condition == 'no':
          run_again = False
          print("GoodBye.")
