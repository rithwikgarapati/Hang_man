import random

# Reading words from a file and storing it in an array
words = []
with open("words.txt", "r") as file1:
    line = file1.readline().strip()
    words.append(line)

    while line:
        line = file1.readline().strip()
        words.append(line)

    file1.close()

# Generating a random word from the array
rand_word = words[random.randint(0, len(words))]

# The random word is now in a list separated by each letter.
rand_word = list(rand_word.upper())

# assigning the number of _ to the guess initially
guess_word = "_" * len(rand_word)

# Now storing the guess word in an array
guess_word = list(guess_word)

# An array of words that are already guessed.
already_guessed = []

# Number of guesses.
num_guesses = 6


# Checking if the length of the word is correct.
def correct_length(u_input):
    if len(u_input) > 1:
        return True
    return False


# Checking if only a single letter is entered not 2 or three.
def is_numeric(u_input):
    if u_input.isnumeric():
        print("Invalid Input.")
        return True
    return False


while num_guesses != 0:

    print(' '.join(guess_word))
    print(f"you have {num_guesses} guesses left.")
    user_input = input("Please enter a single letter or whole word: ")
    user_input = user_input.upper()

    if is_numeric(user_input):
        print("please try again")
        continue

    if user_input in already_guessed:
        print("You already guessed this word. Please try again")
        continue

    elif user_input in rand_word:
        for i in range(len(rand_word)):
            if rand_word[i] == user_input:
                guess_word[i] = user_input

        already_guessed.append(user_input)

    elif correct_length(user_input):
        if user_input == ''.join(rand_word):
            break
        else:
            num_guesses -= 1

    else:
        num_guesses -= 1
        already_guessed.append(user_input)

    if "_" not in guess_word:
        break


if num_guesses == 0:
    print("You are out of tries. The word is " + ''.join(rand_word))
else:
    print("You guessed " + ''.join(rand_word) + " right in " + str(6 - num_guesses) + " Tries.")

print("Game Over")

