import random


word_list = ["cricket", "football", "kabbadi", "kho kho", "badminton", "boxing"]


def get_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(displayed)


def play_hangman():
    word = get_random_word()  
    guessed_letters = set()  
    incorrect_guesses = 0  
    max_incorrect_guesses = 6  

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter '{guess}' is not in the word.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word!")
            break

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
    
