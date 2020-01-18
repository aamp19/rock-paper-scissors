import random
def rockpaperscissors():
    flag = True
    while(flag == True):
        print("What do you choose? ")
        choice = input()
        if (choice == "q"):
            flag = False
            break
        comp = random.randint(1,3)
        if (comp == 1):
            print("rock")
        elif (comp == 2):
            print("paper")
        else:
            print("scissors")
        print(result(choice,comp))
        
def result(user,cpu):
    if (user == 'rock' and cpu == 1 or user == 'scissors' and cpu == 3 or user == 'paper' and cpu == 2):
        return("Tie");

    elif(user == 'rock' and cpu == 3 or user == 'scissors' and cpu == 2 or user == 'paper' and cpu == 1):
        return("you win")

    elif(cpu == 1 and user == 'scissors' or cpu == 3 and user == 'paper' or cpu == 2 and user == 'rock'):
        return("you lose")
    elif(user == 'q'):
        exit()
 
