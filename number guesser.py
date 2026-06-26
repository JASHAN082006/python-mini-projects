import random
print("Number Guessing Game")
secret_number = random.randint(1, 100)
attempts = 0
guess = None 

while guess != secret_number:
    try:
        user_input = input("Guess a number (1-100): ")
        guess = int(user_input)
        attempts += 1  
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
    except ValueError:
        print("Please enter a valid number.")
print(f"Correct! You found it in {attempts} attempts.")