# We are creating a 'Hangman' game. 
import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.



# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# Print "Right" if it is. Print "Wrong" if it's not.

display = "" 
backup = []
n = 10

while n > 0:
 guess = input("Guess a letter -> ").lower()  # Since we have lower case in 'word_list'.
 for char in chosen_word:
     if char == guess:
        display += guess
     else:
        display += "_"
     backup.append(display)

print(display)
# Step 2

# TODO 1 : Create a "placeholder" with the same number of blanks as the 'word_list'. i.e create "_" for each letter in 'word_list'.

# TODO 2 : Create a "Display" that puts the guess letter in the right place. 
