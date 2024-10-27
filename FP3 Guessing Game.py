import random

# Welcome message and get user's choice to play
play = input("Would you like to play a number guessing game? (yes/no): ").lower()

if play != "yes":
    print("Maybe next time!")
else:
    # Generate random number
    secret_number = random.randint(1, 10)
    
    # Initialize guess variable
    guess = 0
    
    print("\nI'm thinking of a number between 1 and 10.")
    
    # Continue loop until correct guess
    while guess != secret_number:
        # Get user's guess
        guess = int(input("\nEnter your guess: "))
        
        # Check if guess is out of range
        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
        # Give feedback based on guess
        elif guess < secret_number:
            print("Too low! Try again!")
        elif guess > secret_number:
            print("Too high! Try again!")
        else:
            print("\nCongratulations! You've guessed the number!")

    # Farewell message
    print("\nThanks for playing! Have a great day!")