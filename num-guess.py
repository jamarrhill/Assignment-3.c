# Name: Jamar Hill
# Date: 10/13/2020
# Description num_guess.py


print("Enter the number for the player to guess.")
guess = int(input())
guess
print("Enter your guess")
pg = int(input())
pg
pg_count = 1
while pg > guess:
        print("Too high - try again")
        pg_count += 1
        pg = int(input())
        pg
while pg < guess:
            print("Too low - try again")
            pg_count += 1
            pg = int(input())
            pg
while pg == guess:
    if pg_count == 1:
                print("You guessed it in", pg_count, "try.")
    else:
        print("You guessed it in", pg_count, "tries.")
        break








