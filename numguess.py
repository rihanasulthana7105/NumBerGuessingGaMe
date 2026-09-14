import random
def play_game():
    #Generate a random target number between 1 and 100
    secret_number=random.randint(1,100)
    attempts=0
    guessed_correctly=False
    print("\n   New Round    ")
    print("I have picked a secret number between 1 and 100.")
    while not guessed_correctly:
        try:
            user_guess=int(input("Enter your guess: "))
            attempts+=1
            if user_guess<secret_number:
                print("Too low!Try again.")
            elif user_guess>secret_number:
                print("Too high!Try again.")
            else:
                print("Congratulations! You guessed it right in attempts: ",attempts)
                guessed_correctly=True
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
def main():
    print("Welcome to the Number Guessing Game!")
    #Loop to allow multipe rounds of play
    while True:
        play_game()
        play_again=input("\nWould you like toplay another round? (yes/no): ")
        if play_again not in ['yes','y']:
            print("Thanks for playing! Goodbye.")
            break
main()
