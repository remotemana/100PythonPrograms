import random

def guess_number():
    while True:  # This starts an infinite loop for the game
        # Random number between 1 and 100
        number_to_guess = random.randint(1, 100) 
        guess = 0 
        attempts = 0

        while guess != number_to_guess: 
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low, try again.")
            elif guess > number_to_guess:
                print("Too high, try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break  # This exits the inner while loop

        # Ask the user if they want to play again
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break  # This exits the outer while loop

if __name__ == "__main__":
    guess_number()
