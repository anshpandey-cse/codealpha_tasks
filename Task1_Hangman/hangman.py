import random

# 5 predefined words
words = ["python", "computer", "programming", "developer", "hangman"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
incorrect_guesses = 0

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect guesses.\n")

while incorrect_guesses < max_attempts:

    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check if word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Take user's guess
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.\n")
        continue

    # Check duplicate guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print(f"Remaining attempts: {max_attempts - incorrect_guesses}\n")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)