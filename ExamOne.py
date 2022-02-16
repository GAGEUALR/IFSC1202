from random import randint
name = input("Enter Your Name: ")

print("Hello, " + name + " You have Five Guesses")

number = randint(1, 20)
guess = 0
timestried = 0

while guess != number:
    guess = int(input("Guess a number: "))
    if guess == number: 
        print("YOU WON, ""Guesses Used: " + str(timestried + 1))
        break
    if guess >= number:
        print("Too High")
        timestried +=1
    if guess <= number:
        print("Too Low")
        timestried +=1
    if timestried == 5:
        print("Sorry " + name + ", You Lost. the number is " + str(number))
        break
        