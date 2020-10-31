import random

def generateNumber():
    a = random.randint(1,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    while a==b or b==c or c==a:
        a = random.randint(1,9)
        b = random.randint(0,9)
        c = random.randint(0,9)
    num = [str(a),str(b),str(c)]
    return num

solved=False
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
print("Code has been generated, please guess a 3 digit number")
number = generateNumber()
print(number)

while solved==False:
    guess=list(input("What is your guess?"))
    print(guess)
    if guess == number:
        print("Congrats! You guessed it!")
        solved = True
        break
    clues = []
    for ind,num in enumerate(guess):
        if num == number[ind]:
            clues.append("Match!")
        elif num in number:
            clues.append("Close!")

    if clues == []:
        clues.append("Nope!")
    else:
        print(clues)