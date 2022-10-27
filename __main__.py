
import random

if __name__ == "__main__":
    IsRunning = True;
    Tries = 0
    RandomNumber = int(random.uniform(1, 9))

    ## Print starter text
    print("Guess a number between 1 to 9.")
    print("You have 3 tries!")

    while(IsRunning):
        try:
            q = int(input("What number: "))
            print(q)

            if(Tries < 2):
                if(q < RandomNumber):
                    Tries += 1
                    print("The answer is greater then your guess.")
                elif(q > RandomNumber):
                    Tries += 1
                    print("The answer is less then you guess.")
                else:
                    print("You got it!")
                    IsRunning = False;
            else:
                print("The answer is " + str(RandomNumber) + "!")
                IsRunning = False;
        except ValueError:
            print("You need to put a integer!")
