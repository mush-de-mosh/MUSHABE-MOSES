import random

ranNo = random.randint(1,10)



while True:
    guess = int(input("Enter your guess"))
    
    if(guess == ranNo):
        print(f"Congragulations!! The number is {guess}")
        break
    elif (guess != ranNo ):
        print("Thats too low.. TRY AGAIN!")
    elif (guess > ranNo):
        print("Thats too high.. TRY AGAIN!")  
    else:
        print("Not even close.. TRY AGAIN!")  