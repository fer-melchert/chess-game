import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        try:
            # Get the user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
