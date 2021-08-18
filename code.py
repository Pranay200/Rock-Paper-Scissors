import random
game_list = ['Rock','Paper', 'Scissors']
computer=c=0
command=p=0
print("Score: Computer"+str(c)+"Player"+str(p))

run=True
while run:
    computer_choice=random.choice(game_list)
    command=input("Rock, Paper, Scissors or Quit: ")
    if command == computer_choice:
        print("TIE")
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print("Player won!")
            p+=1
        else:
            print("Computer won!")
            c+=1
    elif command == 'Paper':
        if computer_choice == 'Rock':
            print("Player won!")
            p+=1
        else:
            print("Computer won!")
            c+=1
    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print("Player won!")
            p+=1
        else:
            print("Computer won!")
            c+=1
    elif command == 'Quit':
        break
    else:
        print("Wrong Command!")
    print("Player: "+command)
    print("Computer: "+computer_choice)
    print("Score: Computer "+str(c)+" Player "+str(p))
    print("")
