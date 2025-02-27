import random
from colorama import Fore

def number_guessing_game():
    print(Fore.CYAN + "\nWelcome to the number guessing game!")
    print(Fore.MAGENTA + "There is a secret number between 1-20. Can you guess it?\n") 

    # Generate the random secret number between 1-20
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input(Fore.YELLOW + "Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print(Fore.RED + "Too low! Try again.\n")
            elif guess > secret_number: 
                print(Fore.RED + "Too high! Try again.\n")
            else:
                print(Fore.GREEN + f"Congratulations! 🎉 You guessed the secret number in {attempts} attempts.\n")
                break  # Exit the loop when guessed correctly

        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")  # Fix indentation


if __name__ == "__main__": 
    number_guessing_game()
