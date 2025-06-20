import random

print("welcome to the number guessing game!")
print("iam thinking of a num between 1 to 100")
num = random.randint(1,100)
level = input("choose a level of difficulty. easy or hard:\n").lower()
if level == "easy":
    i=10
    while i>=1:
        guess = int(input(f"u have {i} attempts left. guess the number:\n"))
        if num>guess:
            print("higher!")
            i-=1
        elif num<guess:
            print("lower!")
            i-=1
        elif num==guess:
            print("perfect! u guessed it!")
            break
    else:
        print("sorry! failed attempts!")
else:
    i=5
    while i>=1:
        guess = int(input(f"u have {i} attempts left. guess the number:\n"))
        if num>guess:
            print("higher!")
            i-=1
        elif num<guess:
            print("lower!")
            i-=1
        elif num==guess:
            print("perfect! u guessed it!")
            break
    else:
        print("sorry! failed attempts!")
        

    