from random import randint
min = 1
max = 99

cor = False

while cor == False:
    rand = randint(min , max)
    print(rand)

    inp = input()
    
    if inp == "b":
        min = rand+1
        #if cor is bigger than rand then why have rand in possible future guesses 
    elif inp == "k":
        max = rand-1
    elif inp == "d":
        cor = True
        