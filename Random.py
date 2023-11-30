import random

secreat_number = random.randint(1,100)
attempt = 0

print("welcome to the new gameing world")
print("I've selected a random number between 1 and 100. Try to guess it.")

while True:
        guess = int(input("Enter your Guess : "))
        attempt += 1

        if guess == secreat_number:
            print("Congratulations! You guessed", secreat_number, "in", attempt)
            break 
        elif guess > secreat_number:
          print("Try lower No.")
        else:  
           print("Try higher No.")

print("Thanks for Playing")
