import random

board = [[" " for row in range(5)] for column in range(5)]

words = ["fable","faced","facer","faces","facet","facia", "earls","early"]

computer = random.choice(words)

turn = 0

right_words = []

# Adding the correct answer in a list to make checking easier
for word in computer:

    right_words.append(word)

wrong_words = []

# Presenting rules of the game
print()
print("THE WORDLE GAMEEEEEEEE: Guess the five letter word to win!!!")
print("==================================================")
print("The rules are as follows: lowercase letter ('a') = right word, wrong place.\n"
       "uppercase letter ('A') = right word, right place, AND!! you only get 5 turns\n")
print("==================================================")
print()
# Added this here so it doesn't always initialize to zero during each turn
row = 0

while turn < 5:

    column = 0

    user_input = input("Enter text:\t")

    # Loop for when users word is more or less than 5
    while len(user_input) != 5:

        print("Your word must be 5 letters")

        user_input = input("Enter text:\t")

    # Updating board based on whether users word is in computer or not
    for word in user_input:

        if word == word in computer:
            # Updating board letter by letter // idk if its efficient or not
            board[row][column] = word

            print(f"'{word}' is in board,", end = ' ', sep = ',')

            column += 1

        else:
            wrong_words.append(word)

            column += 1

    # Checking the location of each word and uppercasing it if it's in the right location
    correct_guess = str

    for checker in range(len(right_words)):

        if right_words[checker] == board[row][checker]:

            letter = board[row][checker]

            board[row][checker] = letter.upper()

            correct_guess = ''.join(board[row][:])

        # Condition to check if you've won within the turns
        if correct_guess == computer.upper():

            turn = 5

    print(f"\nList of wrong words you've tried:\t{wrong_words}")

    for rows in range(5):

        print(board[rows][:])

    row += 1

    turn += 1
print()
print(f"'{computer}' was the word")
print(f"\nList of wrong words you've tried:\t{wrong_words}")







