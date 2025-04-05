import random

print("Welcome to the Number Guessing Game 🎲")
number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("🎉 You guessed it right! The number was", number)
else:
    print("❌ Wrong guess! The number was", number)
