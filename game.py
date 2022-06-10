b = True
while b == True:
    g =[ "R","P","S"]
    print ("Starting game")
    print("this is a rock,paper or scissors game")
    print("R for rock, P for paper, S for scissors")
    a = input("select R, P, or S: ")
    for letter in a:
        if letter in g:
            continue
        else:
            break
    
    import random
    computer_choice = random.choice(g)
    print('your choice is: ', a)
    print('computer_choice is ', computer_choice)
    if a == computer_choice:
        print('It is a tie')
    elif a == 'R' and computer_choice == 'P':
        print ('computer wins')
    elif a == 'P' and computer_choice == 'R':
        print ('congratulations you win')
    elif a == 'R' and computer_choice == 'S':
        print ('congratulations you win')
    elif a == 'S' and computer_choice == 'R':
        print ('computer wins')
    elif a == 'P' and computer_choice == 'S':
        print ('computer wins')  
    elif a == 'S' and computer_choice == 'P':
        print ('congratulations you win')
    elif a not in g:
        print('wrong input')
    print ('do you want to play again, y or n')
    c = input ('enter y to continue or n to end: ')
    if c == 'y':
        continue 
    else:
        break
