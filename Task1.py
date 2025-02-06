import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'computer']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # You can change the number to adjust difficulty
    game_over = False
    
    print("Welcome to Hangman!")
    
    while not game_over:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        if guess.isalpha() and len(guess) == 1:
            guessed_letters.append(guess)
            
            if guess in word:
                print(f"Good guess! The letter '{guess}' is in the word.")
            else:
                incorrect_guesses += 1
                print(f"Oops! The letter '{guess}' is not in the word.")
        else:
            print("Please enter a valid letter.")
        
        if display_word(word, guessed_letters) == word:
            print(f"\nCongratulations! You've guessed the word: {word}")
            game_over = True
        elif incorrect_guesses >= max_incorrect_guesses:
            print(f"\nGame Over! The word was: {word}")
            game_over = True

if __name__ == "__main__":
    hangman()
