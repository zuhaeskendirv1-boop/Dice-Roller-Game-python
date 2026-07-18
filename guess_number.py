import random
num = (random.randint(1, 100))
while True:
    
    player = int(input("Guess the number between 1-100: "))
    if player>100 or player < 1:
        print("This number is out of range. Exiting...")
        break

    if player < num:
        print("Guess higher!")
    elif player > num:
        print("Guess lower!")
    else:
        print("Congratulations, You got it!")
        break